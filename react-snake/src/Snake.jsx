import React from 'react'
import { useState, useRef, useEffect } from 'react'
import { Button } from '@mui/material';

export default function Snake() {

  const canvasElement = useRef()
  let [use, setUse] = useState("hi2")

  return (
    <>
      <h1>Snake</h1>
      <input ref={canvasElement} tabIndex="0" onKeyPress={ () => setUse(canvasElement) } style={{border:"1px solid blue"}} />
      <h1>{use}</h1>
      <Button onclick={() => canvasElement.focus()}>hi</Button>
    </>
  )
}