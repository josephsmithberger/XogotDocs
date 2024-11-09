# Working with Source Control in Xogot

To work with Godot projects stored in Git, Xogot recommends using [Working Copy](https://workingcopyapp.com), a native iOS Git client that integrates seamlessly with the Files App, making it an excellent tool for managing source control on your iPad.

## Cloning an Existing Project

Working Copy can clone a repository directly into Xogot’s projects area, enabling you to use Git to manage your game source code on your iPad. Here’s how to do it:

1. **Open Working Copy** on your iPad.
2. Tap the **“+” button** to add a new repository.
3. Choose **“Clone Repository”** and enter the repository’s URL or use a service integration (e.g., GitHub, GitLab).
4. **Set the destination folder**:
   - When setting the Clone repository options, tap **“Working Copy”** next to “Files app Location.”
   - Navigate to **“On My iPad”** and select the **“Xogot”** folder as the destination.
5. Tap **“Clone”** to initiate the cloning process. Working Copy will create a linked repository within the Xogot projects folder, allowing you to commit, push, and fetch changes directly into Xogot.

**After Cloning**: 
- **Restart Xogot** to make the newly cloned project appear in the project manager:
   - Double-tap the **Home button** (or swipe up from the bottom) and swipe away Xogot.
   - Relaunch **Xogot** to load the cloned project.

## Setting Up a New Project in Git

If you’ve created a new project in Xogot and want to manage it with Git, or you’ve copied a project into Xogot that was already versioned with Git, you can add the project to Working Copy as a Linked Repository:

### Linking a Project in Xogot to Working Copy

1. **Open Working Copy** and tap the **“+” button**.
2. Select **“Add Existing Folder”**.
3. Navigate to **“On My iPad”** and find the **“Xogot”** folder.
4. Select the folder containing your Xogot project and confirm the addition.
5. Working Copy will recognize the project and create a linked repository.

### Adding a Remote 

If the project is not yet connected to a remote repository or you are creating a new repository:

1. **Open the newly linked repository** in Working Copy.
2. Tap **“Add Remote”** under the Remotes section and enter the remote repository URL and authentication details.
3. If the folder is not already a Git repository, tap **“Create Repository”** to create a new repository to host the project
    - Provide a name for the repository.  The default will the be the name of hte linked folder
    - Choose whether the project should be Private or Public
    - Tap **Confirm Create** to finish creating the repository

Once these steps are complete, you can use **Working Copy** to manage version control, perform commits, and push changes. Xogot will automatically reflect file changes due to its integration with the Files App.

## Committing and Pushing Changes with Working Copy

Once you've made changes to your Xogot project, you can use **Working Copy** to manage commits and push updates to your remote repository.

1. **Open Working Copy** and navigate to your linked repository.
2. Working Copy will automatically detect changes in the project folder.
3. To commit changes:
   - Tap on **"Commit"** to view all modified files.
   - Select the files you want to include in the commit.
   - Add a meaningful commit message.
   - Optionally, you can turn on the **Push** toggle to automatically push your changes.
   - Tap **"Commit"** to confirm the commit.

For more detailed instructions on using Working Copy, refer to the [official documentation](https://workingcopyapp.com/manual/) for an in-depth guide on committing, pushing, branching, and other Git operations.
