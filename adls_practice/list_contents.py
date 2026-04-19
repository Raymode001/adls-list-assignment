from azure.storage.blob import BlobServiceClient

def main():
    # Define the blob service URL
    service_url = "https://azurepublicdatasettraces.blob.core.windows.net/"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient(account_url=service_url)

    # Define the container name
    container_name = "azurepublicdataset"

    # List all blobs in the container
    container_client = blob_service_client.get_container_client(container_name)

    print(f"Listing files in {container_name} container with .csv.gz ending")
    for blob in container_client.list_blobs():
        if blob.name.endswith('.csv.gz'):
            print(blob.name)

if __name__ == "__main__":
    main()