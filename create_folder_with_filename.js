import fs from "fs";
import path from "path";

const filepath = "D:\\DESEMBER KAB JEPARA\\KEC KALINYAMATAN";
const files = fs.readdirSync(path.join(filepath));

function splitext(filepath) {
  let index = filepath.lastIndexOf(".");
  if (index === -1) {
    return [filepath, ""];
  } else {
    return [filepath.slice(0, index), filepath.slice(index)];
  }
}

files.forEach((file) => {
  const [filename] = splitext(file);
  fs.mkdirSync(path.join(filepath, filename));
  fs.copyFileSync(
    path.join(filepath, file),
    path.join(filepath, filename, file)
  );
  fs.unlinkSync(path.join(filepath, file));
});
