import { accessSync, renameSync, readdirSync, rename, lstatSync } from "fs";
import { join } from "path";
import { naturalCompare, splitext } from "./const.js";

const path = "/Users/agungfir/Downloads/TAMBAHAN 3/SEPTEMBER/KAB. PATI";
// const files = readdirSync(join(path)).sort(naturalCompare);
const folders = readdirSync(join(path)).sort(naturalCompare).filter(folder => lstatSync(join(path, folder)).isDirectory())

folders.forEach((folder) => {
  const files = readdirSync(join(path, folder)).sort(naturalCompare).filter(file => file.includes('.pdf'))
  files.forEach((file) => {
    const [filename, ext] = splitext(file);
    let newFilename
    if (filename.includes('KEL.')) {
      newFilename = filename.substring(filename.indexOf('KEL. ') + 5, filename.indexOf('KEC'));
      // console.log(newFilename)
    } else {
      newFilename = filename.substring(filename.indexOf('KEL ') + 4, filename.indexOf('KEC'));
      // console.log(newFilename)
    }
    // const newFilename = filename.split(' ')[1]
    // console.log(filename);
    // renameSync(
    //   join(path, folder, file),
    //   join(path, folder, `KAB. PATI-${folder}-${newFilename}${ext}`)
    // );
    renameSync(
      join(path, folder, file),
      join(path, folder, `${filename.trim().toUpperCase()}${ext}`)
    );
  });
});

// files.forEach((file) => {
//   //   const kota = file.split("-")[0];
//   //   const kec = file.split("-")[1];
//   // const desa = file.split("-")[2].split(".")[0];
//   // const kec = file.split("~")[0];
//   // const desa = file.split("~")[1].split(".")[0];
//   const [filename, ext] = splitext(file);
//   // renameSync(join(path, file), join(path, `${kota}-${kec}-${desa}.pdf`));
//   // renameSync(join(path, file), join(path, `KAB. TEGAL-${kec}-${desa}${ext}`));
//   renameSync(
//     join(path, file),
//     join(path, `KAB. BLORA-TUNJUNGAN-${filename}${ext}`)
//   );

//   // try {
//   //   // accessSync(join(path, folder, "BAST.pdf"));
//   //   const [filename, ext] = splitext(file);
//   //   console.log(ext);
//   //   // renameSync(
//   //   //   join(path, file),
//   //   //   join(path, `KOTA SEMARANG-TUGU-${filename}${ext}`)
//   //   // );
//   //   // renameSync(
//   //   //   join(path, folder, "BAST.pdf"),
//   //   //   join(path, folder, "BAST DESA.pdf")
//   //   // );
//   // } catch (e) {
//   //   console.log(file);
//   // }
//   // const files = readdirSync(join(path, folder)).sort(naturalCompare);
//   // try {
//   //   accessSync(join(path, folder, "SPTJM.pdf"));
//   // } catch (e) {
//   //   console.log(folder);
//   // }
// });
