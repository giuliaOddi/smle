Quick Start
===========

Installation
------------

.. code-block:: bash

    pip install smle

Basic Usage Steps
-----------------

1. Initialize a Project
^^^^^^^^^^^^^^^^^^^^^^^

Run the CLI tool to generate a template and config file:

.. code-block:: bash

    smle init

2. Write Your Code
^^^^^^^^^^^^^^^^^^

Use the ``@app.entrypoint`` decorator. Your configuration variables are automatically passed via ``args``.

.. code-block:: python

    from smle import SMLE

    app = SMLE()

    @app.entrypoint
    def main(args):
        # 'args' contains your smle.yaml configurations
        print(f"Training with learning rate: {args['training']['lr']}")

        # Your logic here...

    if __name__ == "__main__":
        app.run()

3. Run It
^^^^^^^^^

.. code-block:: bash

    python main.py

Configuration (``smle.yaml``)
-----------------------------

SMLE relies on a simple YAML structure. You can generate a blank template using:

.. code-block:: bash

    smle create yaml

Contributing
------------

Contributions are welcome! If you have ideas for improvements, feel free to fork the repository and submit a pull request.

#. Fork the Project
#. Create your Feature Branch (``git checkout -b feature/AmazingFeature``)
#. Commit your Changes (``git commit -m 'Add some AmazingFeature'``)
#. Push to the Branch (``git push origin feature/AmazingFeature``)
#. Open a Pull Request