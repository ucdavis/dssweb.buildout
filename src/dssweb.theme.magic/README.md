dss-plone-sandbox
=================

Sandbox repository

Key:
- Carol McMasters-Stone (CMS)
- Jeremy Phillips (JP)
- Regan King (RAK)

Sandbox themes include:

- Twitter Bootstrap Example (CMS) [example]
- UCDavis Responsive Basic (CMS) [ucdavis.responsive]
- UCDavis Wire Frames (RAK) [ucdavis.wireframe]

UCDavis Wire Frames include:

ucdavis.wireframe/
  assets/ - style sheets and fonts
  images/ - images
  config.rb - compass configuration file. We use 'compass watch' to monitor and compile scss to css
  js/ - javascript files
  js/bootstrap/ - bootstrap modules
  js/contrib/ - contributed javascript libraries
  js/*something else* - custom javascript
  manifest.cfg - Diazo theme/package info file
  rules.xml - Diazo rules file
  sass/ - SASS files
    _ucd-variables.scss
    _variables.scss
    abstractions/ - SASS function
    components/ - Modular features, e.g., typography, calendar, chart, block
    sections/ - Page or section specific CSS
    styles.scss - Bootstrap styles [DO NOT edit]
    vendor/ - Third party SASS
      _bootstrap-override-variables.scss - Moved out of _variables.scss; override bootstrap here
      _bootstrap_overrides.scss - Override bootstrap CSS here
  Templates/ - Dreamweaver templates
  index.html - Template 1 wireframe
  t1_charts.html - Chart feature proof page
  t2_ourpeople.html - Template 2 wireframe
  t3_bio.html - Template 3 wireframe
  *something else* - other template files.