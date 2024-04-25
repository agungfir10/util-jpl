import { readFileSync, writeFileSync } from "fs";
import { join } from 'path';
import readline from "readline";
import { google } from "googleapis";

const SCOPES = ["https://www.googleapis.com/auth/drive.file"];
const TOKEN_PATH = "data/TOKEN.json";
const CLIENT_SECRET = ""
const CLIENT_ID = ""
const REDIRECT_URIS = []

const oAuth2Client = new google.auth.OAuth2(
  CLIENT_ID,
  CLIENT_SECRET,
  REDIRECT_URIS
);

function getAccessToken() {
  try {
    const res = readFileSync(TOKEN_PATH)
    return JSON.parse(res.toString())
  } catch (e) {
    return getNewToken()
  }
}

function getNewToken() {
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: "offline",
    scope: SCOPES,
  });
  console.log("Autorisasi dengan mengunjungi: ", authUrl);

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.question("Masukkan kode autentikasi disini: ", (code) => {
    rl.close();
    oAuth2Client.getToken(code, (err, token) => {
      if (err) return console.error("Error retrieving access token", err);

      oAuth2Client.setCredentials(token);
      try {
        writeFileSync(TOKEN_PATH, JSON.stringify(token));
        return token
      } catch (e) {
        console.log('Gagal menyimpan token!')
      }
    });
  });
}

function authorize(token) {
  oAuth2Client.setCredentials(JSON.parse(token));
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
