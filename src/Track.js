import React from 'react';
import VideoSnippetSelector from './VideoSnippetSelector';
import PlayPause from './PlayPause';
import './Track.scss';

const Track = () => {
  return (
    <div className="new-component-container">
      <div className="album-container">
        <img src="./logo.svg" alt="Sample" />
      </div>
      <VideoSnippetSelector />
      <PlayPause />
      <button className="match-button">Match</button>
    </div>
  );
};

export default Track;