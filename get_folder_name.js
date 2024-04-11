import fs from "fs";
import path from "path";
import { exec, execSync } from "child_process";
import { naturalCompare } from "./const.js";

const pathfolder =
  "D:\\EKS KARESIDENAN PATI\\BAPANG ALOKASI OKTOBER\\KAB KUDUS";
const folders = fs.readdirSync(pathfolder).sort(naturalCompare);

folders.forEach((folder) => {
  exec(`dir /b "${path.join(pathfolder, folder)}"`, (err, stdout) => {
    fs.appendFile("desa.txt", stdout, (err) => {});
  });
});
