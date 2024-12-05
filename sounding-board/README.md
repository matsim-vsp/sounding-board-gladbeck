# VSP Sounding Board

Live at <https://vsp.berlin/sounding-board>

Add new boards on the VSP public-svn at

- `public-svn/matsim/scenarios/countries/de/berlin/projects/sounding-board/`

### Build instructions

Requires NodeJS 16.x and Python 3.10. Newer versions don't work!

- Clone the repo
- `nvm use 16`  (install nvm first using npm install -g nvm)
- `pyenv install 3.10` to install Python 3.10
- `pyenv local 3.10` to use 3.10
- `npm ci` to install project dependencies
- `npm run serve` to run your dev server

We don't have GitHub actions set up. To push a build live:
- `npm run deploy`


If you move the build to a different URL you need to change the base prefix in
- `vite.config.js`
- `public/404.html`

Have fun,

Billy
