import { google } from "googleapis";
import { OAuth2Client } from "google-auth-library";
import credentials from "./client_secret.json" assert { type: "json" };

const { client_secret, client_id, redirect_uris } = credentials.web;

const refresh_token =
  "1//0g6QKAjLn8HHzCgYIARAAGBASNwF-L9Ir6bnHk-5Gu8s0i4ff9-LHc1bJEHY2IIRJFMWJKLXv4hBTWmdHl43lOitJk8liRXT2Prg";

const oauth2Client = new OAuth2Client(client_id, client_secret, redirect_uris);
oauth2Client.setCredentials({ refresh_token });

async function refreshToken() {
  try {
    const response = await oauth2Client.refreshAccessToken();
    console.log(response);
    // const accessToken = response.credentials.access_token;
    const accessToken = response.res.data.access_token;
    console.log(`Access token refreshed: ${accessToken}`);
  } catch (error) {
    console.error(`Error refreshing token: ${error}`);
  }
}

refreshToken();
