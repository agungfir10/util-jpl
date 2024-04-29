import { accessSync, renameSync, readdirSync, rename, lstatSync } from "fs";
import { join } from "path";
import { naturalCompare, splitext } from "./const.js";

const path = "/Users/agungfir/Downloads/TAMBAHAN 1/NOVEMBER/KAB. PATI";
// const files = readdirSync(join(path)).sort(naturalCompare);
const folders = readdirSync(join(path)).sort(naturalCompare).filter(folder => lstatSync(join(path, folder)).isDirectory())

folders.forEach((folder) => {
  const files = readdirSync(join(path, folder)).sort(naturalCompare).filter(file => file.includes('.pdf'))
  files.forEach((file) => {
    const [filename, ext] = splitext(file);
    let newFilename
    const filenameUpper = filename.toUpperCase();
    if (filenameUpper.includes('KEL.')) {
      newFilename = filenameUpper.substring(filenameUpper.indexOf('KEL. ') + 5, filenameUpper.indexOf('KEC'));
      console.log(newFilename)
    } else {
      newFilename = filenameUpper.substring(filenameUpper.indexOf('KEL ') + 4, filenameUpper.indexOf('KEC'));
      console.log(newFilename)
    }
    // const newFilename = filename.split(' ')[1]
    // console.log(filename);
    renameSync(
      join(path, folder, file),
      join(path, folder, `KAB. PATI-${folder}-${newFilename.trim()}${ext}`)
    );
    // renameSync(
    //   join(path, folder, file),
    //   join(path, folder, `${filename.trim().toUpperCase()}${ext}`)
    // );
  });
});

// files.forEach((file) => {
//   if (file.includes('.pdf')) {

//     const kota = file.split("-")[0].trim();
//     const kec = file.split("-")[1].trim();
//     // const desa = file.split("-")[2].trim();
//     const desa = file.split("-")[2].split(".")[0].trim();
//     // const kec = file.split("~")[0];
//     // const desa = file.split("~")[1].split(".")[0];
//     const [filename, ext] = splitext(file);
//     renameSync(join(path, file), join(path, `${kota}-${kec}-${desa}${ext}`));
//   }
//   // renameSync(join(path, file), join(path, `KAB. TEGAL-${kec}-${desa}${ext}`));
//   // renameSync(
//   //   join(path, file),
//   //   join(path, `KAB. BLORA-TUNJUNGAN-${filename}${ext}`)
//   // );

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
