import { test, request } from '@playwright/test';

test('CV pom test', async ({ page }) => {
  await page.goto('https://testdevlab.com');


//         page.element({"text": {"value": "Contact us", "case_sensitive": False}}).click()
//         page.element({"text": "Accept"}).click()
//         print(cv_pom_driver.get_page().elements(None))
//         page = cv_pom_driver.get_page()
//         page.element({"text": {"value": "Full Name", "case_sensitive": False}}).send_keys("John Doe")
//
//         page.element({"text": {"value": "Business E-mail", "case_sensitive": False, "contains": True}}).send_keys("johndoe@example.com")
//         page.element({"text": {"value": "Message", "case_sensitive": False, "contains": True}}).send_keys("This is a test message")
  console.log(await parseQuery(page, {"text": {"value": "Contact us", "case_sensitive": false}}))
  console.log(await parseQuery(page, {"text": "Accept"}))

  var contact_us = await parseQuery(page, {"text": {"value": "Contact us", "case_sensitive": false}})
  await page.mouse.click(contact_us.center[0], contact_us.center[1])
  var accept_btn = await parseQuery(page, {"text": "Accept"})
  await page.mouse.click(accept_btn.center[0], accept_btn.center[1])
});


// HELPERS FOR CV_POM

async function parseQuery(page: any, query: object): Promise<any> {
  let i: number = 1;
  while (i < 10) {
    const buffer = await page.screenshot();

    var response = await getCVPOM(buffer.toString('base64'), query)
    for (const obj of response) {
        return obj;
    }
    i++
  }
  
  return false;
}


async function getCVPOM(filedata: string, query: object): Promise<any> {
  const context = await request.newContext();
  
  var raw = {
    "ocr": {'paragraph': false},
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
