// HELPERS FOR CV_POM
import { request } from "@playwright/test";

export function myUtilityFunction() {
  // Function implementation
}

export async function parseQuery(page: any, query: object): Promise<any> {
  let i: number = 1;
  while (i < 10) {
    const buffer = await page.screenshot();

    var response = await getCVPOM(buffer.toString("base64"), query);
    for (const obj of response) {
      return obj;
    }
    i++;
  }

  return false;
}

async function getCVPOM(filedata: string, query: object): Promise<any> {
  const context = await request.newContext();

  var raw = {
    ocr: { paragraph: false },
    image_base64: filedata,
    query: query,
  };

  const response = await context.post(
    "http://localhost:8000/convert_to_cvpom",
    {
      data: raw,
      headers: {
        accept: "application/json",
      },
    },
  );

  return await response.json();
}
