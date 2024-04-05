import { test, request } from '@playwright/test';

test('CV pom test', async ({ page }) => {
  await page.goto('https://flutter-gallery-archive.web.app/');

  // Click cookies.
  await page.locator('#cookie-consent').click();

  console.log(await hasLabel(page, 'rally-main'))
  console.log(await hasLabel(page, 'shrine-main'))
  var rally_button = await hasLabel(page, 'rally-main')
  await page.mouse.click(rally_button.center[0], rally_button.center[1])
  var login_button = await hasLabel(page, 'rally-login-btn')
  await page.mouse.click(login_button.center[0], login_button.center[1])
});


// HELPERS FOR CV_POM

async function hasLabel(page: any, targetLabel: string): Promise<any> {
  let i: number = 1;
  while (i < 10) {
    const buffer = await page.screenshot();
    var query: object = { "label": targetLabel }
    var response = await getCVPOM(buffer.toString('base64'), query)
    for (const obj of response) {
      if (obj.label === targetLabel) {
        return obj;
      }
    }
    i++
  }
  
  return false;
}


async function getCVPOM(filedata: string, query: object): Promise<any> {
  const context = await request.newContext();
  
  var raw = {
    "ocr": false,
    "image_base64": filedata,
    "query": query
  };

  const response = await context.post('http://localhost:8000/convert_to_cvpom', {
        data: raw,
        headers: {
            "accept": "application/json"
        }
    });

    return await response.json()
}
