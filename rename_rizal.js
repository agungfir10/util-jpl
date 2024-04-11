import fs from "fs";
import path from "path";

const pathFolder = process.argv[2];

const folders = fs.readdirSync(pathFolder);

folders.forEach((folder) => {
  const files = fs.readdirSync(path.join(pathFolder, folder));
  fs.renameSync(
    path.join(pathFolder, folder, files[0]),
    path.join(pathFolder, folder, "DTT.pdf")
  );
});
