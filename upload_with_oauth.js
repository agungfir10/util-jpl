import fs from "fs";
import readline from "readline";
import { google } from "googleapis";
import credentials from "./client_secret.json" assert { type: "json" };

const SCOPES = ["https://www.googleapis.com/auth/drive.file"];
const TOKEN_PATH = "token.json";

const { client_secret, client_id, redirect_uris } = credentials.web;
const oAuth2Client = new google.auth.OAuth2(
  client_id,
  client_secret,
  redirect_uris
);

function authorize() {
  fs.readFile(TOKEN_PATH, (err, token) => {
    if (err) return getAccessToken(oAuth2Client);
    oAuth2Client.setCredentials(JSON.parse(token));
  });
}

function getAccessToken(oAuth2Client) {
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: "offline",
    scope: SCOPES,
  });
  console.log("Authorize this app by visiting this url:", authUrl);

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.question("Enter the code from that page here: ", (code) => {
    rl.close();
    oAuth2Client.getToken(code, (err, token) => {
      if (err) return console.error("Error retrieving access token", err);
      oAuth2Client.setCredentials(token);
      fs.writeFile(TOKEN_PATH, JSON.stringify(token), (err) => {
        if (err) return console.error(err);
        console.log("Token stored to", TOKEN_PATH);
      });
      callback(oAuth2Client);
    });
  });
}

function refreshToken() {
  oAuth2Client.refreshAccessToken((err, credentialsResult) => {
    if (err) console.log("Error : ", err);
  });
}

function uploadFile(auth) {
  const drive = google.drive({ version: "v3", auth });

  const fileMetadata = {
    name: "example.txt",
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
        console.error("The API returned an error: " + err);
        return;
      }
      console.log("File uploaded: %s", file.data.id);
    }
  );
}

function createFolder(auth) {
  const drive = google.drive({ version: "v3", auth });

  const fileMetaData = {
    name: "Invoices",
    mimeType: "application/vnd.google-apps.folder",
    parents: ["18fjQrbIxDzSFCb8qvMPV3X84JaUgi0p-"],
  };

  drive.files.create(
    {
      resource: fileMetaData,
      fields: "id",
    },
    (err, file) => {
      if (err) {
        console.error("Upload The API returned an error: " + err);
        return;
      }
      console.log("File uploaded: %s", file.data.id);
    }
  );
}

authorize(credentials, createFolder);
