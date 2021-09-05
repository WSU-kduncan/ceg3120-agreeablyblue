!Setup!

Follow these steps to create a git server capable of storing your projects across multiple devices.

1. Create a set of SSH keys, you'll need to store the private key on your local device and the public key on the server account you're trying to store your projects on. 
	
	First (on your local device) use the commands:
	cd ~ (this takes you to your home directory)
	mkdir .ssh (this creates a folder to store your ssh keys)
	cp SSH_PRIVATE_KEY_LOCATION/NAME .ssh (this copies your SSH key into the private key directory)

	Next (on your server device) use the commands: 
	cd ~ (move to your home directory)
	mkdir .ssh (create a folder to store your ssh keys)
	vim authorized_keys (create a text file that stores your authorized keys)
		Once inside the authorized_keys file, paste your SSH public key into the file
		Use esc to enter the command mode for the text editor, then type ":wq" to write your changes to the file and quit the program

2. Make a profile on your local device so you can easily log in to the server
	
	On your local device use the commands: 
	cd ~/.ssh/ (move to the .ssh directory)
	vim config (this creates an editable config file - you'll have to follow the EXACT format that I've written here, it is case sensitive

		Write the following:
		
		Host CHOOSENAME
			HostName SERVERIP
			User	SERVERUSERNAME
			IdentityFile	LOCATION_OF_KEY/KEY_FILE_NAME

	One you've created this config file you can easily log into your server remotely with the command:
	ssh -i username@CHOOSENAME
	
3. Creating a git repository on your server:

	cd ~ (return to home directory)
	mkdir folder_name (creates a new folder)
	cd folder_name.git (navigate to the new folder)
	git init --bare (creates an empty git repository within your folder) 
	
4. Adding your existing project/files to the new git server from your local device:

	Navigate to your existing project folder you would like to push to the git server
	cd/project_path
	git init (setup the folder for use with git)
	git add . (add all items in the folder to the git project)
	git commit -m 'comment for first commit)
	git remote add origin SERVERUSERNAME@CHOOSENAME:folder_name.git (this adds the origin folder that you previously setup on your server)
	git push origin master (this pushes the files in your local folder to the git folder saved on your server)

Once that's all setup you're good to use your server. These commands will be useful for you to know in the future:

git clone - This command allows you to clone an existing repository

git init - This command allows you to initialize a new git folder ( you used it during the tutorial )

git commit - This command creates a new commit that includes a log message you define

git push  - This command allows you to apply your changes to other branches of the project that you've defined. 



