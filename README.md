--notebook-dir=/path/to/your/directory

Embedding Jupyter Lab into an HTML page via an <iframe> can be somewhat complicated due to security measures, such as CORS (Cross-Origin Resource Sharing) policies. However, there are some steps you can take to embed Jupyter Lab into an iframe.
Option 1: Configuring Jupyter Server

The Jupyter server needs to be configured to allow embedding into iframes. You can do this by modifying your Jupyter configuration file. If you haven't already created a Jupyter configuration file, you can generate one using the following command:

bash

jupyter lab --generate-config

This will generate a .jupyter folder in your home directory containing a file named jupyter_notebook_config.py.

Open jupyter_notebook_config.py and add or uncomment the following lines:

python

c.NotebookApp.tornado_settings = {
    'headers': {'Content-Security-Policy': "frame-ancestors 'self' *"}
}

This will allow the notebook to be embedded in an iframe from any origin. To limit it to specific origins, replace the * with the URLs of the origins you want to allow.

After modifying the config, restart your Jupyter Lab server.
Option 2: Use a Reverse Proxy

Another approach to solving CORS issues is to use a reverse proxy, such as Nginx or Apache, to serve both the site containing the iframe and the Jupyter Lab instance.
HTML Code

Once your Jupyter Lab instance is properly configured, you can embed it into your HTML using an <iframe> tag:

html

<iframe src="http://localhost:8888/lab" width="800" height="600"></iframe>

Replace http://localhost:8888/lab with the URL where your Jupyter Lab is running.
Considerations:

    Security: Be cautious when allowing embedding from all origins, as it could expose your Jupyter Lab instance to security risks.

    User Experience: Jupyter Lab is a complex web application designed to run in a full browser window. Embedding it in an iframe may result in a less than optimal user experience.

    Networking: Ensure that the machine where you're hosting the iframe can actually reach the Jupyter Lab URL.

Given your interest in diving deep into subjects, you might find it beneficial to learn more about web security policies, like CORS, and how they interact with web applications like Jupyter Lab. Understanding the underlying mechanisms will give you better control over your setups.