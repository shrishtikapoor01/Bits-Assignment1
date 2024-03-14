import multiprocessing

def chunk_sum(arr_chunk):
    """Function to compute sum of numbers in a chunk."""
    return sum(arr_chunk)

def parallel_sum(arr, num_processes):
    """Function to perform parallel sum of array elements."""
    # Number of elements per chunk
    chunk_size = len(arr) // num_processes

    # Create a list to store results
    results = []

    # Create and start a process for each chunk
    for i in range(num_processes):
        # Determine the start and end indices for the current chunk
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(arr)
        chunk = arr[start:end]

        # Create a process to compute sum of the current chunk
        process = multiprocessing.Process(target=chunk_sum, args=(chunk,))
        process.start()
        process.join()
        results.append(chunk_sum(chunk))

    # Aggregate the results
    total_sum = sum(results)
    print("Total sum:", total_sum)

if __name__ == "__main__":
    # Example array of numbers
    arr = list(range(1, 10001))

    # Number of processes to use
    num_processes = 4

    # Perform parallel sum of array elements
    parallel_sum(arr, num_processes)
