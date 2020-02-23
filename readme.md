#### Add-on for Anki 2.1.21 or newer

- license: see src/LICENSE
- This add-on is untested. Use it at your own risk. Feedback and improvements are welcome.
- This add-on allows you to replace the css files that Anki uses with custom css files. 
- This add-on is not meant to be just installed. This add-on bundles the css files that are part of Anki 2.1.21 beta 1. To get an effect you must modify or replace some css files.
- You can add css files for each version of Anki. E.g. to replace the built-in `editor.css` of Anki 2.1.21 put a file named `editor.css` into the folder `web/css/21/` (from the src subfolder of this repo).
- This add-on only works with Anki 2.1.21 or newer because it relies on [pull request #445](https://github.com/ankitects/anki/commit/990a6c394b0bbb4e7c7f46fef57746501497c45a) from February 2020.
- To load files from the add-on folder into the webview this add-on uses the AddonManager.setWebExports functionality [introduced in March 2019](https://github.com/ankitects/anki/commit/5e90758f3996e2c216ee62274526a4878952b16c)
