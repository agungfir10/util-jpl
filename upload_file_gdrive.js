import fs from "fs";
import { google } from "googleapis";
import readline from "readline";

// Load the credentials from your client_secret.json file
import credentials from "./client_secret_agung.json" assert { type: "json" };

// Set up the OAuth2 Client
const auth = new google.auth.GoogleAuth({
  credentials,
  scopes: "https://www.googleapis.com/auth/drive",
});

// Create a new drive instance
const drive = google.drive({ version: "v3", auth });

// File to upload
const fileMetadata = {
  name: "PENGGANTI.pdf",
  parents: ["18fjQrbIxDzSFCb8qvMPV3X84JaUgi0p-"],
};
const media = {
  mimeType: "application/pdf",
  body: fs.createReadStream("template/PENGGANTI.pdf"),
};

drive.files.create(
  {
    resource: fileMetadata,
    media: media,
    fields: "id",
  },
  (err, file) => {
    if (err) {
      console.error("Error uploading file:", err);
      return;
    }

    // Set the permission to make the file publicly accessible
    drive.permissions.create(
      {
        fileId: file.data.id,
        requestBody: {
          role: "reader",
          type: "anyone",
        },
      },
      (err, permission) => {
        if (err) {
          console.error("Error setting file permission:", err);
          return;
        }
        console.log("File uploaded and set as public, File ID:", file.data.id);
      }
    );
  }
);
