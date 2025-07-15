import pycloudlib
import argparse

def is_ready():
    # create an IBM client. If there is any problem with the SDK library or config, it will throw an exception and
    # return non-zero error code
    pycloudlib.IBM("bartender")

def launch(name):
    ibm = pycloudlib.IBM("bartender")

    daily = ibm.daily_image(release="noble")
    instance = ibm.launch(
        image_id=daily,
        instance_type="bx3d-16x80",
        name=name,
    )
    print(instance._floating_ip["address"])

def delete(name):
    ibm = pycloudlib.IBM("bartender")
    instance = ibm.find_instance(name)
    instance.delete(wait=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help="Name of the IBM cloud instance")
    parser.add_argument("operation", type=str, help="Operation to perform")
    args = parser.parse_args()

    if args.operation == "launch":
        launch(args.name)
    elif args.operation == "delete":
        delete(args.name)
    elif args.operation == "is-ready":
        is_ready()
    else:
        raise Exception("Unsupported operation")