## UPLOAD SO BULOG

https://astridjplb.id/w/proc/proses_simpan_dokumen.php
POST

file: (binary)
userid: GD11040103
tanggal: 2022-09-23
nodoc: SO/12475/09/2023/11060
jenis: 8 | SO-BULOG
kdkantor: 11001

Sukses : 1
Gagal : No Data
Dokumen Sudah Di Upload: 2|2024-03-11

## UPLOAD FOTO DROP POINT

https://astridjplb.id/w/proc/proses_simpan_dokumen.php

file: (binary)
userid: GD11040101
tanggal: 2023-10-07
nodoc: BAST-222311000683-1144
jenis: 4 | FOTO PENYERAHAN DROP POINT (input no.BAST)
kdkantor: 11001

Sukses : 1
Gagal : No Data
Dokumen Sudah Di Upload: 2|2024-03-11

## UPLOAD DTT

https://astridjplb.id/w/proc/proses_simpan_dokumen.php

file: (binary)
userid: GD11040101
tanggal: 2023-12-11
nodoc: DTT-312311000249
jenis: 7 | DTT
kdkantor: 11001

Sukses : 1
Gagal : No Data
Dokumen Sudah Di Upload: 2|2024-03-11

## UPLOAD SPTJM

file: (binary)
userid: GD11040104
tanggal: 2023-11-11
nodoc: DTT-232311005244
jenis: 9 | SPTJM (input nomor-DTT)
kdkantor: 11001

## UPLOAD PENGGANTI

file: (binary)
userid: GD11040104
tanggal: 2023-11-18
nodoc: DTT-232311005244
jenis: 10 | BAST PENGGANTI (input nomor DTT)
kdkantor: 11001

## UPLOAD PERWAKILAN

file: (binary)
userid: GD11040104
tanggal: 2023-11-18
nodoc: DTT-232311005244
jenis: 11 | BAST PERWAKILAN (input nomor DTT)
kdkantor: 11001

## RENAME

1.SO-BULOG
2.DOC OUT BULOG
3.BAST GUDANG
4.SPM
5.BAST SJ
6.BAST PBP
7.DTT/BNBA
8.SPTJM & BAST PENGGANTI
9.BAST PERWAKILAN

## SO-BULOG

KEY

- SO/
- 50/
- S0/
- 50/
- $O/
- $0/

## Level Compression

- screen
- ebook
- printer
- prepress
- default

## Cara Menggunakan

- Pindahkan File PDF yang ingin di kompress ke folder `compress`
- Lalu ketikkan `python

## Download Dan Install

- https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe
- https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs10030/gs10030w64.exe

## Install Module

- pip install pillow
- pip install natsort
- pip install reportlab
- pip install pymupdf

### Buat Folder

- compress, file sumber pdf untuk di kompres
- compressed, hasil kompres pdf
- convert, file sumber gambar untuk di jadikan pdf
- converted, hasil file gambar yang di pdf
- split, file sumber pdf untuk split pdf ke gambar
- splitted, hasil split pdf
- crop, file sumber untuk crop gambar
- cropped, hasil file crop gambar

## KEUPLOAD TANGGAL 6 APRIL 2024

- KAB. DEMAK (14 KECAMATAN) : ALOKASI DESEMBER

  - _KEC. GAJAH_
    - 4 JENIS DOKUMEN (DTT, SPTJM, PENGGANTI, PERWAKILAN)
  - _KEC. GUNTUR_
    - 4 JENIS DOKUMEN (DTT, SPTJM, PENGGANTI, PERWAKILAN)
  - _KEC. KARANGANYAR_
    - 4 JENIS DOKUMEN (DTT, SPTJM, PENGGANTI, PERWAKILAN)
  - _KEC. KARANGTENGAH_
    - 4 JENIS DOKUMEN (DTT, SPTJM, PENGGANTI, PERWAKILAN)
  - _KEC. MRANGGEN_
    - 4 JENIS DOKUMEN (DTT, SPTJM, PENGGANTI, PERWAKILAN)
  - _KEC. WONOSALAM_

  CATATAN :

  - KEC. GAJAH-DESA. BOYOLALI (FILE TIDAK ADA)
  - KEC. GAJAH-DESA. MLEKANG (FILE TIDAK ADA)

- KAB. KENDAL (20 KECAMATAN) : ALOKASI DESEMBER

  - ALL KECAMATAN (KECUALI PATEAN)

  CATATAN: BEBERAPA BERKAS TIDAK ADA (DIREKAP MENYUSUL)

### KEPERLUAN SCRIPT

#### ROTATE PDF

- ROTATE PDF
  - SEMUA FILE PDF YANG ADA DI DIREKTORI
  - SEMUA FILE PDF YANG ADA DI DALAM DIREKTORI-DIREKTORI
  - PAGE TERTENTU
  - `py rotate.py angle direktori|*|**/*`

#### SPLIT PDF

- SPLIT PDF
  - PER FILE PDF
  - SEMUA FILE PDF YANG ADA DI DIREKTORI
  - SEMUA FILE PDF YANG ADA DI DIREKTORI-DIREKTORI
  - `py rotate.py angle direktori|*|**/*`
- MERGE PDF
  - SEMUA FILE YANG ADA DI DIREKTORI
  - SEMUA FILE YANG ADA DI DALAM DIREKTORI-DIREKTORI
  - FILE TERTENTU
  - `py rotate.py angle direktori|*|**/*`

### KEPERLUAN OCR

- MEMINDAHKAN KE DALAM 13 JENIS FILE

### SALAH

KETERANGAN: TAMBAHAN 3 tapi keupload tambahan 2

KAB. SRAGEN-GEMOLONG-GEMOLONG
SUKSES
KAB. SRAGEN-KALIJAMBE-SAREN
SUKSES
KAB. SRAGEN-SAMBUNGMACAN-BANARAN
SUKSES
Selesai...

```
node --stack-size=9999999 upload_dtt_tambahan_3_sep.js "E:\DOKUMEN TAMBAHAN 3 JATENG\DOKUMEN SEPTEMBER TAMBAHAN 3\KOTA PEKALONGAN" && node --stack-size=9999999 upload_sptjm_tambahan_3_sep.js "E:\DOKUMEN TAMBAHAN 3 JATENG\DOKUMEN SEPTEMBER TAMBAHAN 3\KOTA PEKALONGAN" && node --stack-size=9999999 upload_pengganti_tambahan_3_sep.js "E:\DOKUMEN TAMBAHAN 3 JATENG\DOKUMEN SEPTEMBER TAMBAHAN 3\KOTA PEKALONGAN" && node --stack-size=9999999 upload_perwakilan_tambahan_3_sep.js "E:\DOKUMEN TAMBAHAN 3 JATENG\DOKUMEN SEPTEMBER TAMBAHAN 3\KOTA PEKALONGAN"
```

```js
{
  credentials: {
    access_token: 'ya29.a0Ad52N39ohtxMbCB2qgDer1N9Yyru2WIWRV40feOlReibhtrN9cFnOegBeFU3lwAmHL7f7faSbD_0W8oHmlQWutjjGKMlT_9DGtZCyVgxE_dFc-JVQSMigXTc4reZx48izaHd9EZGZC-cs-P3C3xryORwpp5vyHnSd5diaCgYKAZESARMSFQHGX2MiebXdmk3yRjexnKUJ6ZaGtw0171',
    scope: 'https://www.googleapis.com/auth/drive.file',
    token_type: 'Bearer',
    expiry_date: 1713410753009,
    refresh_token: '1//0g6QKAjLn8HHzCgYIARAAGBASNwF-L9Ir6bnHk-5Gu8s0i4ff9-LHc1bJEHY2IIRJFMWJKLXv4hBTWmdHl43lOitJk8liRXT2Prg'
  },
  res: {
    config: {
      retry: true,
      retryConfig: [Object],
      method: 'POST',
      url: 'https://oauth2.googleapis.com/token',
      data: 'refresh_token=1%2F%2F0g6QKAjLn8HHzCgYIARAAGBASNwF-L9Ir6bnHk-5Gu8s0i4ff9-LHc1bJEHY2IIRJFMWJKLXv4hBTWmdHl43lOitJk8liRXT2Prg&client_id=1035086825463-kdsdo7h1hms8ou9ngtn8sq2p4ssa2upl.apps.googleusercontent.com&client_secret=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&grant_type=refresh_token',
      headers: [Object],
      paramsSerializer: [Function: paramsSerializer],
      body: 'refresh_token=1%2F%2F0g6QKAjLn8HHzCgYIARAAGBASNwF-L9Ir6bnHk-5Gu8s0i4ff9-LHc1bJEHY2IIRJFMWJKLXv4hBTWmdHl43lOitJk8liRXT2Prg&client_id=1035086825463-kdsdo7h1hms8ou9ngtn8sq2p4ssa2upl.apps.googleusercontent.com&client_secret=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&grant_type=refresh_token',
      validateStatus: [Function: validateStatus],
      responseType: 'unknown',
      errorRedactor: [Function: defaultErrorRedactor]
    },
    data: {
      access_token: 'ya29.a0Ad52N39ohtxMbCB2qgDer1N9Yyru2WIWRV40feOlReibhtrN9cFnOegBeFU3lwAmHL7f7faSbD_0W8oHmlQWutjjGKMlT_9DGtZCyVgxE_dFc-JVQSMigXTc4reZx48izaHd9EZGZC-cs-P3C3xryORwpp5vyHnSd5diaCgYKAZESARMSFQHGX2MiebXdmk3yRjexnKUJ6ZaGtw0171',
      scope: 'https://www.googleapis.com/auth/drive.file',
      token_type: 'Bearer',
      expiry_date: 1713410753009,
      refresh_token: '1//0g6QKAjLn8HHzCgYIARAAGBASNwF-L9Ir6bnHk-5Gu8s0i4ff9-LHc1bJEHY2IIRJFMWJKLXv4hBTWmdHl43lOitJk8liRXT2Prg'
    },
    headers: {
      'alt-svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000',
      'cache-control': 'no-cache, no-store, max-age=0, must-revalidate',
      'content-encoding': 'gzip',
      'content-type': 'application/json; charset=utf-8',
      date: 'Thu, 18 Apr 2024 02:25:54 GMT',
      expires: 'Mon, 01 Jan 1990 00:00:00 GMT',
      pragma: 'no-cache',
      server: 'scaffolding on HTTPServer2',
      'transfer-encoding': 'chunked',
      vary: 'Origin, X-Origin, Referer',
      'x-content-type-options': 'nosniff',
      'x-frame-options': 'SAMEORIGIN',
      'x-xss-protection': '0'
    },
    status: 200,
    statusText: 'OK',
    request: { responseURL: 'https://oauth2.googleapis.com/token' }
  }
}
```

### UPLOAD DOC

```
node upload_doc.js DTT SEP +1 E:/PATH
```

### UPLOAD

- REKAP LINK ALOKASI
  - SEP
  - OKT
  - NOV
  - DES
- REKAP LINK KOTA
  - SEP
    - KAB. BATANG
    - KAB. BREBES
- REKAP LINK KECAMATAN
  - SEP
    - KAB. BATANG
      - BANDAR
    - KAB. BREBES

## UPLOAD FILE

bun upload_doc.js SEP REG DTT "/Users/agungfir/Downloads/SEPTEMBER/KAB. PATI" && bun upload_doc.js SEP REG SPTJM "/Users/agungfir/Downloads/SEPTEMBER/KAB. PATI" && bun upload_doc.js SEP REG PENGGANTI "/Users/agungfir/Downloads/SEPTEMBER/KAB. PATI" && bun upload_doc.js SEP REG PERWAKILAN "/Users/agungfir/Downloads/SEPTEMBER/KAB. PATI"

## UPLOAD BLANKO

bun upload_all_doc.js SEP +1 SPTJM "/Users/agungfir/Downloads/BLANKO/TAMBAHAN 1/SEPTEMBER/KAB. REMBANG" && bun upload_all_doc.js SEP +1 PENGGANTI "/Users/agungfir/Downloads/BLANKO/TAMBAHAN 1/SEPTEMBER/KAB. REMBANG" && bun upload_all_doc.js SEP +1 PERWAKILAN "/Users/agungfir/Downloads/BLANKO/TAMBAHAN 1/SEPTEMBER/KAB. REMBANG"

## SEPTEMBER

- KAB. BATANG **DONE**
- KAB. BLORA **DONE**
- KAB. BOYOLALI **DONE**
- KAB. BREBES **DONE**
- KAB. DEMAK **DONE**
- KAB. GROBOGAN **DONE**
- KAB. JEPARA **DONE**
- KAB. KARANGANYAR **DONE**
- KAB. KENDAL
- KAB. KLATEN **DONE**
- KAB. KUDUS **DONE**
- KAB. PATI
- KAB. PEKALONGAN **DONE**
- KAB. PEMALANG **DONE**
- KAB. REMBANG **DONE**
- KAB. SEMARANG
- KAB. SRAGEN **DONE**
- KAB. SUKOHARJO
- KAB. TEGAL **DONE**
- KAB. WONOGIRI **DONE**
- KOTA PEKALONGAN **DONE**
- KOTA SALATIGA **DONE**
- KOTA SEMARANG
- KOTA SURAKARTA **DONE**
- KOTA TEGAL

## OKTOBER

- KAB. BATANG **DONE**
- KAB. BLORA
- KAB. BOYOLALI **DONE**
- KAB. BREBES **DONE**
- KAB. DEMAK **DONE**
- KAB. GROBOGAN 
- KAB. JEPARA
- KAB. KARANGANYAR
- KAB. KENDAL
- KAB. KLATEN
- KAB. KUDUS
- KAB. PATI
- KAB. PEKALONGAN
- KAB. PEMALANG
- KAB. REMBANG
- KAB. SEMARANG
- KAB. SRAGEN
- KAB. SUKOHARJO
- KAB. TEGAL
- KAB. WONOGIRI
- KOTA PEKALONGAN
- KOTA SALATIGA
- KOTA SEMARANG
- KOTA SURAKARTA
- KOTA TEGAL

### CATATAN

- DTT TAMBAHAN 3 NOVEMBER PAKAI TAMBAHAN 2 NOVEMBER
- KECAMATAN TERAKHIR KC PATI UPLOAD TANGGAL 29-04-2024

