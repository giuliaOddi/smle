from smle.utils import set_seed
from smle import entrypoint

@entrypoint
def main(args):

    set_seed(args["training"]["seed"])

    # ========================================
    # TODO: ADD YOUR CODE HERE
    # ========================================

if __name__ == "__main__":
    main()