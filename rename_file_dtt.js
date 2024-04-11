import fs from "fs";
import path from "path";

const filepath = "";
const folders = fs.readdirSync(path.join(filepath));

folders.forEach((folder) => {
  console.log(folder);
  const files = fs.readdirSync(path.join(filepath, folder));
  files.forEach((file) => {
    fs.renameSync(
      path.join(filepath, folder, file),
      path.join(filepath, folder, "DTT.pdf")
    );
  });
});
