import url from "url";

export const __dirname = url.fileURLToPath(new URL(".", import.meta.url));

export function naturalCompare(a, b) {
  const collator = new Intl.Collator(undefined, {
    numeric: true,
    sensitivity: "base",
  });
  return collator.compare(a, b);
}

export function containsNumberLoop(str) {
  for (var i = 0; i < str.length; i++) {
    if (!isNaN(parseInt(str[i]))) {
      return true;
    }
  }
  return false;
}

export function formatDate(date) {
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const year = date.getFullYear();

  return `${year}-${month}-${day}`;
}

export function splitext(filepath) {
  let index = filepath.lastIndexOf(".");
  if (index === -1) {
    return [filepath, ""];
  } else {
    return [filepath.slice(0, index), filepath.slice(index)];
  }
}
