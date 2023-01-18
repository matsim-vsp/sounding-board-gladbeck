# VSP Sounding Board

Live at <https://vsp.berlin/sounding-board>

Add new boards on the VSP public-svn at 

- `public-svn/matsim/scenarios/countries/de/berlin/projects/sounding-board/`

### Build instructions

Requires NodeJS 16.x and yarn: Install Node for your platform, and then `npm install -g yarn`

- Clone the repo
- `yarn install`
- `yarn serve` to run a local dev server
- `yarn build` to build for production

The code assumes the site `prefix` is set to `/sounding-board`, this is added to every URL. To move
the site to a different prefix, edit two files:
- `public/404.html`
- `vite.config.hs`

Have fun,

Billy


