## PART-1

This task was pretty easy and quick to do because all it required was cloning the GitHub repository and creating a new directory in the same repository.
 	
## COMMANDS LEARNT

	git clone <url>: Clones the repository from the specified url.

	mkdir <directory_name> : Used to create directories (folders) in a repository. 
  
## PART-2

The subsequent parts were fun to do as it involved finding files using the clues and executing them to get the secret code. I got the value of x as 6 , as 6 is the first perfect number, i.e. a number whose sum of divisors excluding the number itself is equal to the number. Also , by differentiating the given equation wrt x and substituting the value of x in it to find the value of y , I was able to decode the file which contained the secret code.

## COMMANDS LEARNT
	
	cd <directory_path>: Changes the current working directory to the specified path.
	
	ls -la : To fetch the list of files in the directory

	python3 [filename] : To run a python file

	
## PART-3

In the next challenge, the atomic number of the element that was first used to make semiconductors , which is Germanium was used, with its atomic number being 32 , with the digit at units place taken as y and digit at tens place taken as x.

## COMMANDS LEARNT

	git branch -a : lists all available branches in the respitory

	git checkout <branch_name>: Switched between branches

## PART-4

To start with this part, all we had to do was first switch to a branch which was named after the subject taught by Professor Lupin at Hogwarts. I found out that the subject was " Defence Against The Dark Arts". This challenge was purely based on Harry Potter series , although it was a bit confusing in the middle where we had to copy the spell file in another branch to our main branch , and then execute the file to get the secret code. The file was named after a spell used to fight the creature given by the hints , which was Riddikulus.
	
## COMMANDS LEARNT

	git checkout <remote branch> <Relative path of the file to be copied from the other branch>:Used to copy a specific file from another branch (or commit) into your current working branch without switching branches
	
## PART-5

This part was the toughest amongst the all, as it required checking the commit message and code comments to find the hidden spell. It was something relatively new and confused me a bit on the command to use. I had to use git show command to know the file they had changed, which was supposedly the file where the secret code is hidden, 'Priori Incantatem.py'.
	
## COMMANDS LEARNT

	git log : Used to view the commit history of a repository. It displays a list of commits in reverse chronological order (most recent commits first).

	git show --name-only <commit-hash> : The git show command displays detailed information about a specific commit. Adding the --name-only option lists only the file names changed in the commit.


	
## PART-6

This part marked the end of the task where all I had to do was join all the codes I had found earlier to get the secret code. Using echo command , I decoded the code in a readable format and got the link to the final github repository which contained the congratulatory message and that marked the end of my task.

Here is the link I got after decoding the secret code:
https://github.com/TheHuntsman4/TheFinalSpell
	
## COMMANDS LEARNT

	echo "commit-hash" | base64 --decode : Decodes the Base64-encoded string into a readable format.

	git add [filename]: Stages the specified file for commit.

	git status: Displays the files that have been modified.

	git branch: Lists all available branches in the repository.

	git push: Pushes the local branch's changes to the remote repository.
	

## OVERALL EXPERIENCE

The task was pretty fun, and the way it led to clues, was very engaging. I thoroughly enjoyed this task, and this has to be my favourite task among all, mainly considering that this was the first task I started with, and this motivated me a lot. Though I was confused a bit at times, this was one of the easiest tasks to start with and I had a great time doing them.

