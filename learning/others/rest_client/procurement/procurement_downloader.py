import requests
import json
import os
import zipfile
import logging
import csv
import xml.etree.ElementTree as ET


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_directories():
    """Create necessary directories if they don't exist."""
    directories = ['downloads', 'unzips']
    for directory in directories:
        if os.path.exists(directory):
            # Remove all files in the directory
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    import shutil
                    shutil.rmtree(file_path)
            logger.info(f"Cleaned directory: {directory}")
        else:
            os.makedirs(directory)
            logger.info(f"Created directory: {directory}")


def download_file(url, filename):
    """
    Download a file from the given URL.

    Args:
        url (str): The URL to download from
        filename (str): The name to save the file as

    Returns:
        bool: True if download was successful, False otherwise
    """
    try:
        # Clean the filename by removing everything after '.zip'
        if '.zip' in filename.lower():
            filename = filename[:filename.lower().find('.zip') + 4]

        response = requests.get(url, stream=True)
        response.raise_for_status()

        filepath = os.path.join('downloads', filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        logger.info(f"Downloaded: {filename}")
        return True
    except Exception as e:
        logger.error(f"Error downloading {filename}: {str(e)}")
        return False


def extract_zip(zip_path):
    """
    Extract a zip file to the unzips directory.

    Args:
        zip_path (str): Path to the zip file

    Returns:
        bool: True if extraction was successful, False otherwise
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Create a subdirectory with the zip filename (without extension)
            extract_dir = os.path.join(
                'unzips',
                os.path.splitext(os.path.basename(zip_path))[0]
            )
            os.makedirs(extract_dir, exist_ok=True)
  
            zip_ref.extractall(extract_dir)
            logger.info(f"Extracted: {zip_path} to {extract_dir}")
            return True
    except Exception as e:
        logger.error(f"Error extracting {zip_path}: {str(e)}")
        return False


def extract_xml_data(xml_file):
    """Extract relevant data from XML file."""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Define namespace maps for different possible structures
        namespaces = {
            'ted': (
                'http://enotice.service.gov.uk/resource/schema/UK/'
                'R2.0.9/publication'
            ),
            'ns1': (
                'http://publications.europa.eu/resource/schema/ted/'
                'R2.0.9/publication'
            ),
            'def': (
                'http://publications.europa.eu/resource/schema/ted/'
                '2016/nuts'
            )
        }

        data = {
            'date_pub': '',
            'official_name': '',
            'town': '',
            'title': '',
            'short_descr': ''
        }

        # Try different paths for each field with different namespaces
        for ns_prefix, ns_uri in namespaces.items():
            ns = {ns_prefix: ns_uri}

            # Date publication
            paths = [
                f'.//{ns_prefix}:COMPLEMENTARY_INFO/'
                f'{ns_prefix}:DATE_DISPATCH_NOTICE',
                f'.//{ns_prefix}:NOTICE_DATA/{ns_prefix}:DATE_DISPATCH',
                f'.//{ns_prefix}:PUBLICATION/{ns_prefix}:DATE_PUB'
            ]
            for path in paths:
                elem = root.find(path, ns)
                if elem is not None and elem.text:
                    data['date_pub'] = elem.text.strip()
                    break

            # Official name
            paths = [
                f'.//{ns_prefix}:CONTRACTING_BODY/'
                f'{ns_prefix}:ADDRESS_CONTRACTING_BODY/'
                f'{ns_prefix}:OFFICIALNAME',
                f'.//{ns_prefix}:ADDRESS_CONTRACTING_BODY/'
                f'{ns_prefix}:OFFICIALNAME',
                f'.//{ns_prefix}:CONTRACTING_AUTHORITY/'
                f'{ns_prefix}:OFFICIALNAME'
            ]
            for path in paths:
                elem = root.find(path, ns)
                if elem is not None and elem.text:
                    data['official_name'] = elem.text.strip()
                    break

            # Town
            paths = [
                f'.//{ns_prefix}:CONTRACTING_BODY/'
                f'{ns_prefix}:ADDRESS_CONTRACTING_BODY/{ns_prefix}:TOWN',
                f'.//{ns_prefix}:ADDRESS_CONTRACTING_BODY/{ns_prefix}:TOWN',
                f'.//{ns_prefix}:CONTRACTING_AUTHORITY/{ns_prefix}:TOWN'
            ]
            for path in paths:
                elem = root.find(path, ns)
                if elem is not None and elem.text:
                    data['town'] = elem.text.strip()
                    break

            # Title
            paths = [
                f'.//{ns_prefix}:OBJECT_CONTRACT/{ns_prefix}:TITLE/'
                f'{ns_prefix}:P',
                f'.//{ns_prefix}:OBJECT_CONTRACT/{ns_prefix}:TITLE',
                f'.//{ns_prefix}:TITLE/{ns_prefix}:P'
            ]
            for path in paths:
                elem = root.find(path, ns)
                if elem is not None and elem.text:
                    data['title'] = elem.text.strip()
                    break

            # Short description
            paths = [
                f'.//{ns_prefix}:OBJECT_CONTRACT/{ns_prefix}:SHORT_DESCR/'
                f'{ns_prefix}:P',
                f'.//{ns_prefix}:OBJECT_CONTRACT/{ns_prefix}:SHORT_DESCR',
                f'.//{ns_prefix}:SHORT_DESCR/{ns_prefix}:P'
            ]
            for path in paths:
                elem = root.find(path, ns)
                if elem is not None and elem.text:
                    data['short_descr'] = elem.text.strip()
                    break

        # Only return data if we found at least some information
        if any(data.values()):
            return data
        return None

    except ET.ParseError as e:
        logger.error(f"Error parsing XML file {xml_file}: {e}")
        return None
    except Exception as e:
        logger.error(f"Error extracting data from XML file {xml_file}: {e}")
        return None


def save_to_csv(data_list, output_file):
    """
    Save extracted data to a CSV file, overwriting any existing content.

    Args:
        data_list (list): List of dictionaries containing the extracted data
        output_file (str): Path to the output CSV file
    """
    if not data_list:
        logger.warning("No data to save to CSV")
        return

    fieldnames = ['date_pub', 'official_name', 'town', 'title', 'short_descr']

    try:
        # Remove existing file if it exists
        if os.path.exists(output_file):
            os.remove(output_file)
            logger.debug(f"Removed existing file: {output_file}")

        # Create new file with write mode
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)
        logger.info(f"Data saved to CSV: {output_file}")
    except Exception as e:
        logger.error(f"Error saving CSV file: {str(e)}")


def process_xml_files(month_year):
    """
    Process all XML files in the unzips directory and extract required 
    information.

    Args:
        month_year (str): Month and year in format 'month-year' 
            (e.g., 'february-2025')
    """
    extracted_data = []
    xml_count = 0

    # Walk through all subdirectories in the unzips folder
    for root, _, files in os.walk('unzips'):
        # Check if the current directory matches the month_year
        if month_year.lower() in root.lower():
            for file in files:
                if file.endswith('.xml'):
                    xml_path = os.path.join(root, file)
                    try:
                        data = extract_xml_data(xml_path)
                        if data:
                            extracted_data.append(data)
                        xml_count += 1
                        if xml_count % 100 == 0:
                            logger.info(f"Processed {xml_count} XML files")
                    except Exception as e:
                        logger.error(f"Error processing {xml_path}: {str(e)}")

    if not extracted_data:
        logger.warning("No data was extracted from XML files")
    else:
        logger.info(f"Successfully processed {xml_count} XML files")
        logger.info(f"Extracted {len(extracted_data)} records with data")

    # Save the extracted data to CSV
    output_file = f"procurement_data_{month_year}.csv"
    save_to_csv(extracted_data, output_file)


def process_procurement_data(month_year):
    """
    Process procurement data for a specific month and year.
    
    Args:
        month_year (str): Month and year in format 'month-year' 
            (e.g., 'february-2025')
    """
    # Create necessary directories
    create_directories()
    
    # Construct the API URL
    base_url = (
        "https://ckan.publishing.service.gov.uk/api/action/package_search"
    )
    params = {
        'fq': f'name:uk-public-procurement-notices-{month_year}'
    }
    
    try:
        # Fetch data from the API
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('result', {}).get('results'):
            logger.error(f"No results found for {month_year}")
            return
        
        # Get resources from the first result
        resources = data['result']['results'][0].get('resources', [])
        
        if not resources:
            logger.error(f"No resources found for {month_year}")
            return
        
        # Download and extract each resource
        for resource in resources:
            url = resource.get('url')
            if not url:
                continue
                
            # Generate filename from URL
            filename = url.split('/')[-1]
            if '.zip' in filename.lower():
                filename = filename[:filename.lower().find('.zip') + 4]
            
            # Download the file
            if download_file(url, filename):
                # Extract if it's a zip file
                if filename.endswith('.zip'):
                    zip_path = os.path.join('downloads', filename)
                    extract_zip(zip_path)
        
        # Process all XML files after downloading and extracting
        process_xml_files(month_year)
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from API: {str(e)}")
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON response: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    # List of months
    months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    
    # Get current date
    from datetime import datetime
    current_date = datetime.now()
    
    # Calculate default month and year
    if current_date.month == 1:  # If current month is January
        default_month = "december"
        default_year = current_date.year - 1
    else:
        default_month = months[current_date.month - 2]  # Previous month
        default_year = current_date.year
    
    # Print available months
    print("\nAvailable months:")
    for i, month in enumerate(months, 1):
        print(f"{i}. {month.capitalize()}")
    
    # Get user input with default values
    while True:
        try:
            default_month_num = months.index(default_month) + 1
            prompt = f"\nEnter month number (1-12) [{default_month_num}]: "
            month_num = input(prompt).strip()
            if not month_num:  # If empty, use default
                month_num = str(default_month_num)
            
            month_num = int(month_num)
            if 1 <= month_num <= 12:
                break
            print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            year = input(f"Enter year [{default_year}]: ").strip()
            if not year:  # If empty, use default
                year = str(default_year)
            
            year = int(year)
            if 2000 <= year <= 2100:  # Reasonable year range
                break
            print("Please enter a year between 2000 and 2100.")
        except ValueError:
            print("Please enter a valid year.")
    
    # Construct month_year string
    month_year = f"{months[month_num - 1]}-{year}"
    print(f"\nProcessing data for {months[month_num - 1].capitalize()} {year}")
    process_procurement_data(month_year)
