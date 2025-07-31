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
    print(f"{instance._floating_ip['address']}\t{instance._instance['id']}")

def delete(instance_id):
    ibm = pycloudlib.IBM("bartender")
    instance = ibm.get_instance(instance_id)
    instance.delete(wait=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=str, help="ID of the IBM cloud instance")
    parser.add_argument("operation", type=str, help="Operation to perform")
    args = parser.parse_args()

    if args.operation == "launch":
        launch(args.id)
    elif args.operation == "delete":
        delete(args.id)
    elif args.operation == "is-ready":
        is_ready()
    else:
        raise Exception("Unsupported operation")
