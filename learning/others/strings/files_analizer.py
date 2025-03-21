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
                    # Get the path prefix (n or p)
                    prefix = line.split('/')[0]
                    # Extract product name from the path
                    product = line.split('/')[-1].replace('.yaml', '')
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
                    # Get the path prefix (n or p)
                    prefix = line.split('/')[0]
                    # Split the path
                    parts = line.split('/')
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
                    # Get the path prefix (n or p)
                    prefix = line.split('/')[0]
                    # Split the path
                    parts = line.split('/')
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


# Example usage
if __name__ == "__main__":
    # Test the function
    file_path = "files.txt"
    
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
    
    # Display results grouped by path prefix
    print("Products grouped by path prefix:")
    for prefix in ['n', 'p']:
        if product_groups[prefix]:
            print(f"\n{prefix.upper()}:")
            for product in sorted(product_groups[prefix]):
                print(f"- {product}")
    
    print("\nClusters grouped by path prefix:")
    for prefix in ['n', 'p']:
        if cluster_groups[prefix]:
            print(f"\n{prefix.upper()}:")
            for cluster in sorted(cluster_groups[prefix]):
                print(f"- {cluster}")
    
    print("\nCluster-Product combinations grouped by path prefix:")
    for prefix in ['n', 'p']:
        if combination_groups[prefix]:
            print(f"\n{prefix.upper()}:")
            for cluster, product in sorted(combination_groups[prefix]):
                print(f"- Cluster: {cluster}, Product: {product}")
