from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000},reduced_motion='reduce')
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:5173')
 page.screenshot(path='/tmp/vampire-desktop.png',full_page=True)
 page.get_by_role('button',name='How to play').click()
 assert page.locator('dialog').is_visible()
 page.keyboard.press('Escape')
 for key,title in [('1','You got the night shift.'),('2','Meet the new management.'),('3','A very narrow escape.')]:
  page.get_by_role('button',name='Enter the interview' if key=='1' else 'Try another fate').click()
  page.get_by_role('button',name='Inspect the study').click()
  assert page.locator('dialog').is_visible()
  page.keyboard.press('Escape')
  for _ in range(6):page.keyboard.press(key)
  assert page.get_by_role('heading',name=title).is_visible()
 assert page.get_by_text('3 of 3 endings discovered').is_visible()
 page.reload()
 page.set_viewport_size({'width':390,'height':844})
 page.screenshot(path='/tmp/vampire-mobile.png',full_page=True)
 assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
 page.get_by_role('button',name='Enter the interview').click()
 for _ in range(6):page.locator('[data-choice="0"]').click()
 assert page.get_by_role('heading',name='You got the night shift.').is_visible()
 page.get_by_role('button',name='Enable sound').click()
 assert page.get_by_role('button',name='Mute sound').get_attribute('aria-pressed')=='true'
 assert not errors,errors
 browser.close()
 print('PASS: three endings, replay, saved collection, dialogs, keyboard, mobile, sound control, no browser errors')
