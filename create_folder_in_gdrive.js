import { google } from "googleapis";
import fs from "fs";

// Load the credentials from your client_secret.json file
const credentials = JSON.parse(fs.readFileSync("client_secret.json"));

// set up the OAuth2 Client
const auth = new google.auth.GoogleAuth({
  credentials,
  scopes: "https://www.googleapis.com/auth/drive",
});

// Create a new drive instance
const drive = google.drive({ version: "v3", auth });

// Define the ID of the public folder where you want to create the new folder
const parentFolderId = "18fjQrbIxDzSFCb8qvMPV3X84JaUgi0p-";

// Create a folder in Google Drive within the specified parent folder
function createFolderInParent(name, parentFolderId) {
  drive.files.create(
    {
      resource: {
        name: name,
        mimeType: "application/vnd.google-apps.folder",
        parents: [parentFolderId],
      },
    },
    (err, file) => {
      if (err) {
        console.error("Error creating folder:", err);
        return;
      }
      console.log("Folder created in parent folder:", file.data);
    }
  );
}

// Call the createFolderInParent function with the desired folder name and parent folder ID
createFolderInParent("My New Folder", parentFolderId);
