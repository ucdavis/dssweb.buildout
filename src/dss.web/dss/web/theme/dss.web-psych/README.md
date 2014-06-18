Cake Farm Wireframe Sandbox
=================

Wire Frames structure:

<ul>
  <li>dss.web/dss/web/theme/dss.web-psych/
    <ul>
      <li>assets/ - style sheets and fonts</li>
      <li>images/ - images</li>
      <li>config.rb - compass configuration file. We use 'compass watch' to monitor and compile scss to css</li>
      <li>js/ - javascript files
        <ul>
          <li>bootstrap/ - bootstrap modules</li>
          <li>contrib/ - contributed javascript libraries</li>
          <li>*something else* - custom javascript</li>
        </ul>
      </li>
      <li>manifest.cfg - Diazo theme/package info file</li>
      <li>rules.xml - Diazo rules file</li>
      <li>sass/ - SASS files
        <ul>
          <li>_ucd-variables.scss - branding related variables, e.g., color palettes</li>
          <li>_variables.scss - include variable files here</li>
          <li>abstractions/ - SASS functions</li>
          <li>components/ - Modular features, e.g., typography, calendar, chart, block</li>
          <li>sections/ - Page or section specific CSS</li>
          <li>styles.scss - Bootstrap styles [DO NOT edit]</li>
          <li>vendor/ - Third party SASS</li>
          <li>_bootstrap-override-variables.scss - Moved out of _variables.scss; override bootstrap here</li>
          <li>_bootstrap_overrides.scss - Override bootstrap CSS here</li>
        </ul>
      </li>
      <li>static/ - Plone directory (?)</li>
      <li>Templates/ - Dreamweaver templates</li>
      <li>index.html - Template 1 wireframe</li>
      <li>t1_charts.html - Chart feature proof page</li>
      <li>t2_ourpeople.html - Template 2 wireframe</li>
      <li>t3_bio.html - Template 3 wireframe</li>
      <li>*something else* - other custom template files.</li>
    </ul>
  </li>
</ul>