def extract_products(file_path):
    """
    Read files.txt and extract product names from the pattern
    */values/defaults/<product name>.yaml

    Args:
        file_path (str): Path to the files.txt file

    Returns:
        list: List of tuples containing (prefix, product_name)
    """
    products = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                # Check if line matches the pattern
                if '/values/defaults/' in line and line.endswith('.yaml'):
                    # Split the path once and store the result
                    parts = line.split('/')
                    # Get the path prefix (n or p) and product name
                    prefix = parts[0]
                    product = parts[-1].replace('.yaml', '')
                    products.append((prefix, product))

        return products

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def extract_clusters(file_path):
    """
    Read files.txt and extract cluster names from the pattern
    */values/clusters/<cluster name>/<cluster name>.yaml

    Args:
        file_path (str): Path to the files.txt file

    Returns:
        list: List of tuples containing (prefix, cluster_name)
    """
    clusters = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                # Check if line matches the pattern
                if '/values/clusters/' in line and line.endswith('.yaml'):
                    # Split the path
                    parts = line.split('/')
                    # Get the path prefix (n or p)
                    prefix = parts[0]
                    try:
                        # Find the index of 'clusters'
                        cluster_index = parts.index('clusters')
                        # Need at least 2 more parts after 'clusters'
                        if len(parts) > cluster_index + 2:
                            # Get the cluster name from the path
                            cluster_name = parts[cluster_index + 1]
                            # Get the yaml filename
                            yaml_name = parts[-1].replace('.yaml', '')
                            # Only add if cluster name matches the yaml filename
                            if cluster_name == yaml_name:
                                clusters.append((prefix, cluster_name))
                    except (ValueError, IndexError):
                        continue

        return clusters

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def extract_cluster_products(file_path):
    """
    Read files.txt and extract cluster-product combinations from the pattern:
    */values/clusters/<cluster name>/<product name>.yaml

    Args:
        file_path (str): Path to the files.txt file

    Returns:
        list: List of tuples containing (prefix, cluster_name, product_name)
    """
    combinations = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                # Check if line matches the pattern
                if '/values/clusters/' in line and line.endswith('.yaml'):
                    # Split the path
                    parts = line.split('/')
                    # Get the path prefix (n or p)
                    prefix = parts[0]

                    try:
                        # Find the index of 'clusters'
                        cluster_index = parts.index('clusters')
                        # Need at least 2 more parts after 'clusters'
                        if len(parts) > cluster_index + 2:
                            # Get the cluster name from the path
                            cluster_name = parts[cluster_index + 1]
                            # Get the product name from the yaml filename
                            product_name = parts[-1].replace('.yaml', '')

                            # Add if it's not a cluster yaml
                            if cluster_name != product_name:
                                combinations.append((prefix, cluster_name, product_name))
                    except (ValueError, IndexError):
                        continue

        return combinations

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def extract_info(file_path):
    """
    Extract all information from the files.txt file and group it by path prefix.

    Args:
        file_path (str): Path to the files.txt file

    Returns:
        tuple: A tuple containing three dictionaries, each with path prefixes as keys and lists of items as values.
    """
    # Extract all data
    products = extract_products(file_path)
    clusters = extract_clusters(file_path)
    combinations = extract_cluster_products(file_path)

    # Group products by path prefix
    product_groups = {'n': [], 'p': []}
    for prefix, product in products:
        product_groups[prefix].append(product)

    # Group clusters by path prefix
    cluster_groups = {'n': [], 'p': []}
    for prefix, cluster in clusters:
        cluster_groups[prefix].append(cluster)

    # Group combinations by path prefix
    combination_groups = {'n': [], 'p': []}
    for prefix, cluster, product in combinations:
        combination_groups[prefix].append((cluster, product))

    return product_groups, cluster_groups, combination_groups


# Example usage to test the function 
if __name__ == "__main__":
    # Test the function
    file_path = "files.txt"

    product_groups, cluster_groups, combination_groups = extract_info(file_path)

    # Display results grouped by path prefix
    print("Products:")
    for prefix, products in product_groups.items():
        print(f"\t{prefix}: {products}")

    print("\nClusters:")
    for prefix, clusters in cluster_groups.items():
        print(f"\t{prefix}: {clusters}")

    print("\nCluster-Product:")
    for prefix, combinations in combination_groups.items():
        print(f"\t{prefix}: {combinations}")
