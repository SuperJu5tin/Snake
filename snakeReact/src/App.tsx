import { Box, Button, ButtonGroup, Container } from "@mui/material"
import Snake from "./Snake"

function App() {

  return (
    <Box sx={{
      display:"flex",
      margin:"100px"
    }}>
      <Box sx={{
      display:"flex",
      margin:"auto"
    }}>
        <ButtonGroup>
          <Button>Hi</Button>
        </ButtonGroup>
        <Snake />
      </Box>
    </Box>
  )
}

export default App
