---
layout: default
title: "Dart Tutorials"
description: "The Dart Tutorials&mdash;Your guide to building great web apps."
has-permalinks: true
rel:
  author:
    - mary-campione
tutorial:
  id: tut-home
next: get-started/
next-title: "Get Started"
---

{% capture content %}

<img src="images/banner.png">

**The Dart Tutorials** teach you how to build web applications
using the Dart language, tools, and APIs.

<strong>Who are you?</strong>
<ul>
<li> You already know how to program in a structured language like C or Java.</li>
<li> You are familiar with object-oriented programming.</li>
<li> You might not know how to program the browser
     through the DOM (Document Object Model).</li>
</ul>

<strong>Let's go!</strong> Follow the tutorials in order
from left to right...or choose just the ones you need.

<div class="tute-tabs">
<div class="tabbable">
  <ul class="nav nav-tabs">
    <li class="active"><a href="#basics" data-toggle="tab">Get started</a></li>
    <li><a href="#dom" data-toggle="tab">Browser</a></li>
    <li><a href="#packages" data-toggle="tab">Packages</a></li>
    <li><a href="#polymer" data-toggle="tab">Polymer</a></li>
    <li><a href="#forms" data-toggle="tab">Forms & Data</a></li>
    <!--<li><a href="#mobile" data-toggle="tab">Mobile</a></li>-->
  </ul>

  <div class="tab-content">

  <!-- BASICS TAB -->
    <div class="tab-pane active" id="basics">

      Download the software and
      discover which tools and libraries you get with the bundle.
      Run two sample apps.

      <div class="row-fluid">

        <!-- Getting Started -->
        <div class="span6">
          <section>
          <h4><a href="get-started/"><img src="images/target.png" height="20" width="20">&nbsp;Get started</a></h4>
            <p>Get Dart. Run two apps.
            </p>
          <img src="images/clickme-screenshot.png" width="300">
          </section>
        </div>

      </div> <!-- end row-fluid -->
    </div> <!-- end Getting Started tab -->

  <!-- DOM TAB -->
    <div class="tab-pane" id="dom">

      Web pages are programmed in HTML and represented
      within the browser as a tree structure
      called the DOM (Document Object Model).
      Dart apps can modify the DOM programmatically,
      thus dynamically changing the web page.
      First, learn how to connect Dart and HTML.
      Then learn how to add, move, and remove DOM elements.

      <div class="row-fluid">
        <!-- Connect Dart & HTML -->
        <div class="span6">
          <section>
          <h4><a href="connect-dart-html/"><img src="images/target.png" height="20" width="20">&nbsp;Connect Dart &amp; HTML</a></h4>
            <p>Include a Dart script in an HTML page.
            </p>
          <img src="images/miniapp-screenshot.png" width="300">
          </section>
        </div>

        <!-- Add Elements -->
        <div class="span6">
          <section>
          <h4><a href="add-elements/"><img src="images/target.png" height="20" width="20">&nbsp;Add Elements to the DOM</a></h4>
          <p>Add elements to the web page and move them.</p>
          <img src="images/todo-screenshot.png" width="300">
          </section>
        </div>

      </div>


      <div class="row-fluid">
        <!-- Remove Elements -->
        <div class="span6">
          <section>
          <h4><a href="remove-elements/"><img src="images/target.png" height="20" width="20">&nbsp;Remove DOM Elements</a></h4>
          <p>Delete elements from the web page.</p>
          <img src="images/todo-with-delete-screenshot.png" width="300">
          </section>
        </div>
        <div class="span6">
        </div>

      </div> <!-- end row-fluid -->
    </div> <!-- end DOM tab -->

  <!-- PACKAGES TAB -->
    <div class="tab-pane" id="packages">

      Dart developers have been busy creating code libraries that can help you be more productive.
      Leverage that code or put your code out in the world to share with others.

      <div class="row-fluid">

        <!-- Packages -->
        <div class="span6">
          <section>
          <h4><a href="shared-pkgs/"><img src="images/target.png" height="20" width="20">&nbsp;Install Shared Packages</a></h4>
          <p>Organize and share code at <a href="http://pub.dartlang.org/">pub.dartlang.org</a>.</p>
          <img src="images/add-packages-screenshot.png" width="300">
          </section>
        </div>
        <div class="span6">

        </div>
      </div>
    </div> <!-- end Packages tab -->

  <!-- DEPRECATED: WEB UI TAB -->
  <!--
    <div class="tab-pane" id="webui">

<aside class="alert" style="background-color:Lavender;color:SlateBlue">
  <font size="24">
  <i class="icon-bullhorn"> </i>
  </font>
  Web UI is being upgraded to
  <a href="/polymer-dart/" target="_blank">Polymer.dart</a>.
  We've just added a tutorial about
  <a href="/docs/tutorials/polymer/">Polymer Elements</a>,
  one key feature of Polymer.
  We've also provided Polymer.dart versions of the tutorial's Web UI apps.
  Check out the
  <a href="https://github.com/dart-lang/dart-tutorials-samples/tree/master/web/"
         target="_blank">tutorials's code repo</a> on github.
</aside>

      Web components and templates are the next great ideas in web application development.
      Together they provide the building blocks to create richer and more dynamic web applications.
      With the Dart team’s <a href="http://pub.dartlang.org/packages/web_ui">Web UI package</a>,
      you can get started using web components and templates now.

      <div class="row-fluid">

        <div class="span6" style="border-right:1px solid Lavender">
          <section>
          <h4><a href="web-ui/"><img src="images/target.png" height="20" width="20">&nbsp;Get Started with Web UI</a></h4>
          <p>Bind Dart variables to UI elements.</p>
          <img src="images/shout-screenshot.png" width="300">
          </section>
        </div>

        <div class="span6" style="border-right:1px solid Lavender">
          <section>
          <h4><a href="templates/"><img src="images/target.png" height="20" width="20">&nbsp;Use Templates</a></h4>
          <p>Activate UI elements with loops and conditionals.</p>
          <img src="images/hangman-screenshot.png" width="300">
          </section>
        </div>
      </div> 

      <div class="row-fluid">
        <div class="span6">
          <section>
          <h4><a href="custom-elements/"><img src="images/target.png" height="20" width="20">&nbsp;Define a Custom DOM Tag</a></h4>
          <p>Create new HTML tags with custom elements.</p>
          <img src="images/convert-screenshot.png" width="300">
          </section>
        </div>
        <div class="span6">
        </div>
      </div>
    </div>
  -->

  <!-- POLYMER TAB -->
    <div class="tab-pane" id="polymer">
<!--
<aside class="alert" style="background-color:Lavender;color:SlateBlue">
  <font size="24">
  <i class="icon-bullhorn"> </i>
  </font>
  <a href="/polymer-dart/" target="_blank">Polymer.dart</a>.
  supersedes Web UI.
  <a href="/docs/tutorials/polymer/">Polymer Elements</a>,
  a new tutorial, covers one key feature of Polymer.dart.
  We've also provided Polymer.dart versions of the tutorial's Web UI apps.
  Check out the
  <a href="https://github.com/dart-lang/dart-tutorials-samples/tree/master/web/"
         target="_blank">tutorials's code repo</a> on github.
</aside>
-->
      <div class="row-fluid">

        <div class="span6">
          <section>
          <h4><a href="polymer-intro/"><img src="images/target.png" height="20" width="20">&nbsp;Define a Custom Element</a></h4>
          <p>Create a custom HTML element using Polymer.</p>
          <img src="images/stopwatch-screenshot.png" width="200">
          </section>
        </div>

        <div class="span6">
        </div>

      </div>
    </div>

  <!-- FORMS TAB -->
    <div class="tab-pane" id="forms">

      Various classes in the Dart libraries help you get, send, receive,
      and save user data.
      You can use input elements within forms to get data from users.
      You can use JSON to format data and HttpRequest to send requests and receive responses.
      And, finally, you can save data on the client with IndexedDB.

      <div class="row-fluid">

        <!-- Fetch Data -->
        <div class="span6">
          <section>
          <h4><a href="fetchdata/"><img src="images/target.png" height="20" width="20">&nbsp;Fetch Data Dynamically</a></h4>
          <p>Load data from a static file or from a server.</p>
          <img src="images/allaboutyou-screenshot.png" width="300">
          </section>
        </div>

        <!-- Forms -->
        <div class="span6">
          <section>
          <h4><a href="forms/"><img src="images/target.png" height="20" width="20">&nbsp;Get Input from a Form</a></h4>
          <p>Use forms and input elements to get data.</p>
          <img src="images/slambook-screenshot.png" width="300">
          </section>
        </div>
      </div> <!-- end row-fluid -->

      <div class="row-fluid">
        <!-- IndexedDB -->
        <div class="span6">
          <section>
          <h4><a href="indexeddb/"><img src="images/target.png" height="20" width="20">&nbsp;Use IndexedDB</a></h4>
          <p>Save data on the client with IndexedDB.</p>
          <img src="images/countdown-screenshot.png" width="300">
          </section>
        </div>
        <div class="span6">
        </div>
      </div> <!-- end row-fluid -->
    </div> <!-- end FORMS tab -->

  <!-- MOBILE TAB -->
  <!--
    <div class="tab-pane" id="mobile">
      <div class="row-fluid">

        <div class="span6" style="border-right:1px solid Lavender">
          <section>
          <h4><a href="mobile/"><img src="images/target.png" height="20" width="20">&nbsp;Write for Mobile Devices</a></h4>
          <p>Mobile devices are taking over the world!</p>
          <img src="images/countdown-screenshot.png" width="300">
          </section>
        </div>

        <div class="span6">
        </div>

      </div>
    </div>
  -->

  </div> <!-- end tab content-->
</div> <!--end tabbable -->
</div> <!-- end of tute-tabs -->

{% endcapture %}

{% include tutorial_main_page.html %}
