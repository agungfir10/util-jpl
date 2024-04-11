import fs, { accessSync } from "fs";
import path from "path";

const filepath = "E:\\DOKUMEN NOVEMBER REGULER JATENG\\KAB. SEMARANG";
const folders = fs.readdirSync(path.join(filepath));

folders.forEach((folder) => {
  console.log(folder);

  try {
    accessSync(path.join(filepath, folder, "DTT.pdf"));
    fs.renameSync(
      path.join(filepath, folder, "DTT.pdf"),
      path.join(filepath, folder, "DTT-ONLY.pdf")
    );
  } catch (e) {}
});
