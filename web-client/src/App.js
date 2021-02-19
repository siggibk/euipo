import './App.css';
import { Button, Container, Table, TableCell, TableContainer, TableHead, TextField, Paper, TableRow, TableBody, Dialog, DialogTitle, DialogContent, FormControl, InputLabel, Select, MenuItem } from '@material-ui/core';

import { useState } from 'react';
import trademarkRepository from './api/trademarkRepository'
import designRepository from './api/designRepository'

import { TrademarkApplication } from './components/TrademarkApplication';

function App() {
  const [input, setInput] = useState('')
  const [trademark, setTrademark] = useState(null)
  const [trademarks, setTrademarks] = useState([])
  const [design, setDesign] = useState(null)
  const [designs, setDesigns] = useState([])

  const [modalOpen, setModalOpen] = useState(false)
  const [typeFilter, setTypeFilter] = useState('trademark')

  const handleFetch = async () => {
    if (typeFilter === 'trademark') {
      await handleFetchTrademarks()
    } else {
      await handleFetchDesigns()
    }
  }

  const handleFetchTrademarkDetails = async (application_number) => {
    try {
      const { data } = await trademarkRepository.getDetails(application_number)
      setTrademark(data)
      setModalOpen(true)
    } catch (e) {
      console.log('Failed to fetch information about trademark')
    }
  }

  const handleFetchTrademarks = async () => {
    try {
      const filter = {'applicant_identifier': input}
      const { data } = await trademarkRepository.get(filter)
      setTrademarks(data)
    } catch (e) {
      console.log('Failed to fetch information about trademark')
    }
  }

  const handleFetchDesignDetails = async (design_identifier) => {
    try {
      const { data } = await designRepository.getDetails(design_identifier)
      setDesign(data)
      setModalOpen(true)
    } catch (e) {
      console.log('Failed to fetch information about trademark')
    }
  }

  const handleFetchDesigns = async () => {
    try {
      const filter = {'applicant_identifier': input}
      const { data } = await designRepository.get(filter)
      setDesigns(data)
    } catch (e) {
      console.log('Failed to fetch information about trademark')
    }
  }

  const handleTypeChange = async (e) => {
    const value = e.target.value
    setTypeFilter(value)
    
    if (value === 'trademark') {
      await handleFetchTrademarks()
    } else {
      await handleFetchDesigns()
    }
  }

  const onClose = () => {
    setModalOpen(false)
  }

  const trademarkTable = () => {
    return (
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Trademark name</TableCell>
              <TableCell>Status</TableCell>
              <TableCell align="right">Application number</TableCell>
              <TableCell align="right">Status milestone</TableCell>
              <TableCell align="right">Status date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {trademarks.map((row) => (
              <TableRow onClick={() => handleFetchTrademarkDetails(row.application_number)} key={row.application_number}>
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell>{row.status}</TableCell>
                <TableCell align="right">{row.application_number}</TableCell>
                <TableCell align="right">{row.status_milestone}</TableCell>
                <TableCell align="right">{row.status_date}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    )
  }

  const designTable = () => {
    return (
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Indication</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Renewal status</TableCell>
              <TableCell align="right">Design identifier</TableCell>
              <TableCell align="right">Application number</TableCell>
              <TableCell align="right">Status date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {designs.map((row) => (
              <TableRow onClick={() => handleFetchDesignDetails(row.design_identifier)} key={row.design_identifier}>
                <TableCell component="th" scope="row">
                  {row.indication}
                </TableCell>
                <TableCell>{row.status}</TableCell>
                <TableCell align="right">{row.renewal_status}</TableCell>
                <TableCell align="right">{row.design_identifier}</TableCell>
                <TableCell align="right">{row.application_number}</TableCell>
                <TableCell align="right">{row.status_date}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    )
  }


  return (
    <div className="App">
      018307275 86864
        <Container>
          <div className="search-container">
            <TextField
              variant="outlined"
              type="text"
              label="Applicant identifier"
              size="small"
              fullWidth={false}
              onChange={(e) => setInput(e.target.value)}
            />
            <Button className="search-button" onClick={handleFetch} variant="contained" color="primary">Fetch</Button>
          </div>
          <FormControl>
            <InputLabel id="demo-simple-select-label">Type</InputLabel>
            <Select
              labelId="demo-simple-select-label"
              id="demo-simple-select"
              value={typeFilter}
              onChange={handleTypeChange}
            >
              <MenuItem value={'trademark'}>Trademarks</MenuItem>
              <MenuItem value={'design'}>Designs</MenuItem>
            </Select>
          </FormControl>
          <Dialog fullWidth={true} maxWidth="sm" open={modalOpen} onClose={onClose}>
            <DialogContent>
              {trademark ? <TrademarkApplication trademark={trademark} /> : ''}
            </DialogContent>
          </Dialog>
          {typeFilter === 'trademark' ? trademarkTable() : designTable()}
        </Container>
    </div>
  );
}

export default App;
