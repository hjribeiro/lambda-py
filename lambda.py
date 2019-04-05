def func(a, b, operation):
    return operation(a, b)


print(func(2, 10, lambda a, b : a + b))
print(func(2, 10, lambda a, b : a * b))

func("Hello ", "Dan", print)


def upload_file(file, bucket_type):
    print("will upload file")
    bucket_type(file)
    

def upload_to_s3(file):
    print("uploading to S3")

def upload_to_gcp(file):
    print("uploading to GCP")


upload_file("test_file", upload_to_s3)
