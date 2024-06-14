from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

bro = Chrome(options=options)
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

url = "fudan.bbs.kaoyan.com"  # 首页
bro.get("https://www.brownsfashion.com/hk/shopping/y-project-blue-evergreen-maxi-cowboy-straight-leg-jeans-23387182")
bro.implicitly_wait(10)
input()