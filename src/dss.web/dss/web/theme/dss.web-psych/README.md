Cake Farm Wireframe Sandbox
=================

Development notes:
2014-07-25 RAK: Updated styles for the faculty/staff directory tiles template. Added list of templates but this is in flux.
2014-06-27 RAK: Updated basic navigation treatments. Testing on IE9 reveals compatibility issues between Bootstrap collapse and nav functionality.

Wire Frames structure:

<ul>
  <li>dss.web/dss/web/theme/dss.web-psych/
    <ul>
      <li>assets/ - style sheets and fonts
        <ul>
          <li>app.css (new)</li>
          <li>bootstrap.min.css (new)</li>
          <li>foundation.css (new) [check for conflict with app.css]</li>
          <li>topbar.css (new)</li>
        </ul>
      </li>
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
          <li>_settings.scss (new)</li>
          <li>abstractions/ - SASS functions</li>
          <li>components/ - Modular features, e.g., typography, calendar, chart, block</li>
          <li>sections/ - Page or section specific CSS</li>
          <li>app.scss (new)</li>
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
      <li>7/25/2014 RAK: FOLLOWING TEMPLATES CURRENTLY IN FLUX</li>
      <li>t4_adhoc.html (new)</li>
      <li>t5_research.html (new)</li>
      <li>t6_research_area.html (new)</li>
      <li>t7_research_lab.html (new)</li>
      <li>t8_research_project.html (new)</li>
      <li>t9_contact.html (new)</li>
      <li>t10_students.html (new)</li>
      <li>t12_prospective_students.html (new)</li>
      <li>t13_news.html (new)</li>
      <li>t14_events.html (new)</li>
      <li>t15_search.html (new)</li>
      <li>*something else* - other custom template files.</li>
    </ul>
  </li>
</ul>