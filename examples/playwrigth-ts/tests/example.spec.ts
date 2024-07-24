import { test, request } from "@playwright/test";

import { parseQuery } from "../helpers/cv_pom";

test("CV pom test", async ({ page }) => {
  await page.goto("/");

  console.log(
    await parseQuery(page, {
      text: { value: "Contact us", case_sensitive: false },
    }),
  );
  console.log(await parseQuery(page, { text: "Accept" }));

  var contact_us = await parseQuery(page, {
    text: { value: "Contact us", case_sensitive: false },
  });
  await page.mouse.click(contact_us.center[0], contact_us.center[1]);
  var accept_btn = await parseQuery(page, { text: "Accept" });
  await page.mouse.click(accept_btn.center[0], accept_btn.center[1]);
});
