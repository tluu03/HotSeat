import React from 'react';
import ReactDOM from 'react-dom';
import Hotseat from './components/Hotseat'

function init () {
  let app = document.querySelectorAll('[data-section="app"]')[0];
  ReactDOM.render(
    <Hotseat />,
    app
  );
}

// This would usually wait for the ready/DOMContentLoaded
// event, but we're loading this async, and it's up last
init();
