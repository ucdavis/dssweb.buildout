Cake Farm Wireframe Sandbox
=================

Development notes:
2014-09-05 RAK: Updated file structure and Readme. 
2014-07-25 RAK: Updated styles for the faculty/staff directory tiles template. Added list of templates but this is in flux.
2014-06-27 RAK: Updated basic navigation treatments. Testing on IE9 reveals compatibility issues between Bootstrap collapse and nav functionality.

Wire Frames structure:

<ul>
  <li>dss.web/dss/web/theme/dss.web-psych/
    <ul>
      <li>assets/ - style sheets and fonts
        <ul>
          <li>styles.css - primary SASS compiled styles</li>
					<li>sub-org.css - dept., center, institute custom styles</li>
					<li>~~app.css~~</li>
          <li>~~bootstrap.min.css (moved to vendor)~~</li>
          <li>~~foundation.css (moved to vendor)~~</li>
          <li>~~topbar.css (moved to vendor)~~</li>
					<li>~~jquery.cf.happbox.css - used for bounce boxes on homepage~~</li>
					<li>~~chart.css (moved to components)~~</li>
					<li>~~about.css (moved to sections)~~</li>
					<li>~~index.css (moved to sections)~~</li>
					<li>~~ourpeople.css  (moved to sections)~~</li>
					<li>components (new)
						<ul>
							<li>charts.css - css for t1_charts.html (not currently used)</li>
						</ul>
					</li>
					<li>fonts (new)
						<ul>
							<li>bootstrap/ - standard glyphicons</li>
							<li>lucida/</li>
						</ul>
					</li>
					<li>sections (new)
						<ul>
							<li>about.css - about page specific css</li>
							<li>index.css - index page specific css/li>
							<li>ourpeople.css - our people page specific css</li>
						</ul>
					</li>
					<li>vendor (new)
						<ul>
							<li>bootstrap.css</li>
							<li>bootstrap.min.css</li>
							<li>foundation.css</li>
							<li>jquery.cf.happybox.css</li>
							<li>reset.css</li>
							<li>topbar.css</li>
						</ul>
					</li>
					<li>bower_components (new)
						<ul>
							<li>Wallpaper - plugin used for underlay banners. TODO: Compelling reason NOT to move under assets?</li>
						</ul>
					</li>
        </ul>
			</li>

      <li>images/ - images</li>
      <li>config.rb - compass configuration file. We use 'compass watch' to monitor and compile scss to css.</li>
			<li>config.codekit (new) - In local installation using CodeKit to compile. Not in repository. If you experience issues compiling SASS with 
      <li>js/ - javascript files
        <ul>
					<li>chart_effects.js - used for the t1_charts.html animations. Not currently used</li>
					<li>expand.js - used for the dynamic adding and removal of classes for the accordion effect</li>
					<li>jquery.cf.main.js - core custom JavaScript</li>
					<li>jumplinks.js - adds jump links to h3 headers in the about page</li>
					<li>modernizer.min.js - Are we using?</li>
          <li>~~sort.js - for table sorting. Not currently used.~~</li>
					<li>~~tablesorter.min.js - for table sorting. Not currently used.~~</li>
					<li>bootstrap/ - bootstrap modules. TODO: Technically a contrib, so move there.</li>
          <li>contrib/ - contributed javascript libraries. TODO: Cleanup prior to production.
					  <ul>
							<li>backbone-min.js - Not currently used.</li>
							<li>bootstrap.min.js</li>
							<li>Chart.js - used for t1_charts.html template</li>
							<li>html5shiv.min.js - used for ie8 compatibility</li>
							<li>jquery.easing.1.3.js - used for happybox JQuery plugin</li>
							<li>jquery.min.js - jquery library </li>
							<li>respond.min.js - used for ie8 compatability</li>
							<li>underscore-min.js - backbone dependency. Not currently used.</li>						
						</ul>				
					</li>
					<li>foundation/ - Foundation 5.3.0. originally installed via Bower, hence the bower.json file with css, js, and scss dependiencies. TODO: Distribute across asset/vendor and sass folders being careful to resolve duplicate foundation files.
						<ul>
							<li>js/
								<ul>
									<li>foundation/ - TODO: Move needed foundation components to js/contrib
										<ul>
											<li>foundation.topbar.js</li>
											<li>...</li>
										</ul>
									</li>
									<li>vendor/ 
										<ul>
											<li>modernizr.js - if needed, use instead modernizr.min.js in js/</li>
											<li>...</li>
										</ul>
									</li>
									<li>foundation.js - ALL foundation (do not use; instead, using foundation.min.js and component js)</li>
									<li>foundation.min.js - use this</li>
								</ul>
							</li>
							<li>scss/ - move these files to our sass folder if we want to compile foundation instead using the asset/vendor/foundation.css &amp; topbar.css pre-compiled files
								<ul>
									<li>...</li>
								</ul>
							</li>
							<li>bower.json - Bower settings used if this folder maintain using Bower.</li>
						</ul>
					</li>
					<li>min/ - minified custom js files. TODO: Determine where/how this fits in our workflow. </li>
					<li>plugins/ (new)
						<ul>
							<li>jquery.cf.happybox.js - Cake Farm custom plugin for home banner jumping boxes treatment</li>
						</ul>
					</li>
        </ul>
      </li>
      <li>manifest.cfg - Diazo theme/package info file</li>
      <li>rules.xml - Diazo rules file</li>
      <li>sass/ - SASS files
        <ul>
          <li>_ucd-variables.scss - branding related variables, e.g., color palettes</li>
          <li>_variables.scss - include variable files here</li>
          <li>~~_settings.scss~~</li>
          <li>abstractions/ - SASS functions</li>
          <li>components/ - Modular features, e.g., typography, calendar, chart, block</li>
          <li>sections/ - Page or section specific CSS</li>
          <li>~~app.scss~~</li>
          <li>styles.scss - Main styles</li>
					<li>global.scss - Currently not used. TODO: Evaluate origin and remove.</li>
          <li>vendor/ - Third party SASS
						<ul>
							<li>bootstrap/ - bootstrap folder</li>
							<li>bootstrap.scss</li>
	          	<li>_bootstrap-override-variables.scss - Moved out of _variables.scss; override bootstrap here</li>
	          	<li>_bootstrap_overrides.scss - Override bootstrap CSS here</li>
							<li>jquery.cf.happybox.scss - happybox plugin styles</li>
						</ul>
					</li>
					<li>_theme.scss - theme styles</li>
        </ul>
      </li>
      <li>static/ - Plone directory (images and style.css). TODO: Carol, do we need this folder?</li>
      <li>Templates/ - Dreamweaver templates</li>
      <li>index.html - Template 1 wireframe</li>
      <li>t2_ourpeople.html - Template 2 wireframe</li>
      <li>t3_bio.html - Template 3 wireframe</li>
      <li>FOLLOWING TEMPLATES CURRENTLY IN DEVELOPMENT</li>
      <li>t4_adhoc.html</li>
      <li>t5_research.html</li>
      <li>t6_research_area.html</li>
      <li>t7_research_lab.html</li>
      <li>t8_research_project.html</li>
      <li>t9_contact.html</li>
      <li>t10_students.html</li>
      <li>t12_prospective_students.html</li>
      <li>t13_news.html</li>
      <li>t14_events.html</li>
      <li>t15_search.html</li>
			 <li>t1_charts.html - Chart feature proof page. Currently not in use. TODO: Remove</li>
    </ul>
  </li>
</ul>