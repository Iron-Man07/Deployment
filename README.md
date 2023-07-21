#####################################################################################################################################
Deployment Instructions:

'''
Anaconda Installation on Ubuntu

Step 1 - Download and Install Anaconda Scrip:

Once you're logged into your VPS, refresh the APT command to synchronize all repositories via the command line:
~$ sudo apt-get update

Move to the /tmp directory:
~$ cd /tmp

Download the newest Anaconda installer with the wget command. If you don't have it, install it first:
~$ apt-get install wget

Download the Anaconda installer:
~$ wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh

Once the download is complete, verify the hash code integrity of the package:
~$ sha256sum Anaconda3-2022.05-Linux-x86_64.sh

The output will notify if any errors occurred. If there are no errors, move on to the actual installation step. To continue, run the Anaconda bash shell script:
~$ bash Anaconda3-2022.05-Linux-x86_64.sh

If you want to install Miniconda instead, use the following commands consecutively:
~$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
~$ sha256sum Miniconda3-latest-Linux-x86_64.sh
~$ bash Miniconda3-latest-Linux-x86_64.sh

After running the bash command, you'll be welcomed to the Anaconda setup. However, you must review and agree to its license agreement before the installation. Hit Enter to continue.

Pressing the space bar a few times will bring you to the end of the license agreement, where you can accept the terms. Type in “yes” as highlighted and hit Enter.



Step 2 - Choose Installation Directory:

After agreeing to the license terms, the following prompt will ask you to input the directory where to install the Anaconda on the Ubuntu system. The default location is the user's HOME directory on Ubuntu.

It is recommended to have Anaconda installed in this location. Therefore, press Enter to confirm the default location.

In the next prompt, you will see that the installation process has started. Wait a few minutes until the installer successfully completes the installation process. Type “yes” once more and press Enter.

Congratulations, you have successfully installed Anaconda!



Step 3 - Test the Connection

With the installation done, the next step is to activate the added environment settings using the following command:
source ~/.bashrc

Then, test out the connection:
conda info

If the installation process was successful, a piece of similar-looking information should be displayed:


Updating Anaconda

In case you ever need to update Anaconda, start by updating the conda package manager first:
conda update conda

Then, update the actual Anaconda distribution:
conda update anaconda

Wait a few minutes until the installer successfully completes the Anaconda installation process, type “y” and press Enter.


Uninstalling Anaconda

In order to uninstall Anaconda, install the following anaconda-clean package:
conda install anaconda-clean

Lastly, remove all Anaconda-related files and directories:
anaconda-clean


To create an environment with a specific version of python:
conda create --name myenv python=3.9

'''










'''
Launch EC2 instance (Security Groups set)

sudo apt-get update
sudo apt-get install python3-venv
mkdir helloworld
cd helloworld/
python3 -m venv venv
source venv/bin/activate
pip install Flask
sudo nano app.py       (Creating a new file and copy paste some Flask code)
{
    Copy paste the following code:
    --------------------------------------------------------------
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def fun():
        return "RNIL"

    if __name__=='__main__':
        app.run()
    --------------------------------------------------------------
    
    Ctrl + O then Enter   (To save file)
    Ctrl + X
}
cat app.py      (To show file)
python app.py
{
    Ctrl + C
}
pip install gunicorn
gunicorn -b 0.0.0.0:8000 app:app
{
    Ctrl + C
}
sudo nano /etc/systemd/system/helloworld.service         (Editing a file)
{
    Copy paste the following code:
    --------------------------------------------------------------
    [Unit]
    Description=Gunicorn instance for a simple hello world app
    After=network.target
    [Service]
    User=ubuntu
    Group=www-data
    WorkingDirectory=/home/ubuntu/helloworld
    ExecStart=/home/ubuntu/helloworld/venv/bin/gunicorn -b localhost:8000 app:app                       (For Python virtual environment)
                                        (or)
    ExecStart=/home/ubuntu/anaconda3/envs/myenv/bin/gunicorn -b localhost:8000 app:app                  (For Conda virtual environment)
    Restart=always
    [Install]
    WantedBy=multi-user.target 
    --------------------------------------------------------------
    
    Ctrl + O then Enter   (To save file)
    Ctrl + X
}

sudo systemctl daemon-reload
sudo systemctl start helloworld
sudo systemctl enable helloworld
curl localhost:8000

sudo apt-get install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
Copy paste public IP to the browser (It will Show "Welcome to nginx")

sudo nano /etc/nginx/sites-available/default                 (Modify the file)
{
    Copy paste the following code before "server code block":
    --------------------------------------------------------------
    upstream flaskhelloworld {
        server 127.0.0.1:8000;
    }
    
    server {
        ..........
        ..........
    }
    --------------------------------------------------------------

    Copy paste the following code after server_name:
    --------------------------------------------------------------
    location / {
        proxy_pass http://flaskhelloworld;
    }
    --------------------------------------------------------------
    
    Ctrl + O then Enter   (To save file)
    Ctrl + X
}

sudo systemctl restart nginx
Copy paste public IP to the browser (It will Show now our application)



To stop the service and restart after changing files we have to run the following command:
To stop process ------------> sudo systemctl stop helloworld         (helloworld is the "service name in helloworld.service")
Then Run all commands after this command mentioned above





Important Commands:
To see current running processes of gunicorn ------------>   ps ax|grep gunicorn
To stop gunicorn process ----------------> pkill gunicorn
To stop process ------------> sudo systemctl stop helloworld



If error occurred in importing openCV on Ubuntu then run the following comamand:
sudo apt-get update
sudo apt-get install -y python3-opencv
pip install opencv-python

'''
