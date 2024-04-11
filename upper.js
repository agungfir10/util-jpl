import fs from "fs";
import path from "path";
import { splitext } from "./const.js";
const filepath = process.argv[2];

const files = fs.readdirSync(filepath);

files.forEach((file) => {
  const [filename, ext] = splitext(file);
  fs.renameSync(
    path.join(filepath, file),
    path.join(filepath, `${filename.toUpperCase()}${ext}`)
  );
});
