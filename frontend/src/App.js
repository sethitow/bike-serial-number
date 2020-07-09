import React, { useState } from 'react';
import { Container, Grid, Paper, TextField, Button, AppBar, Toolbar, Typography, makeStyles } from '@material-ui/core';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@material-ui/core';

import { gql } from "apollo-boost";
import { useQuery } from '@apollo/react-hooks';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    title: {
        flexGrow: 1,
    },
    table: {
        minWidth: 650,
    },
}));

const GET_BIKE_DATA = gql`
query ($code: String!){
    bikeInfo(serialCode: $code) {
      model
      modelYear
      manufactureMonth
      manufactureYear
      version
      serialNumber
    }
  }   
`

function ResultRow(serialCode) {
    const { loading, error, data } = useQuery(GET_BIKE_DATA, {
        variables: { code: serialCode.serialCode },
    });

    if (loading) return null;
    if (error){
        console.log(JSON.stringify())
    }
    if (error) {
        var error_string = "Error"
        try{
            error_string = String(error.graphQLErrors[0].message)
        }
        catch {}
        return (
        <TableRow key={serialCode.serialCode}>
            <TableCell component="th" scope="row">{serialCode.serialCode}</TableCell>
            <TableCell component="th" scope="row" colSpan={6} ><center>{error_string}</center></TableCell>
        </TableRow>
    )
        }

    function pad(num, size) { return ('000000000' + num).substr(-size); }

    return (
        <TableRow key={serialCode.serialCode}>
            <TableCell component="th" scope="row">{serialCode.serialCode}</TableCell>
            <TableCell>{data.bikeInfo.model}</TableCell>
            <TableCell align="right">{data.bikeInfo.modelYear}</TableCell>
            <TableCell align="right">{data.bikeInfo.manufactureMonth}</TableCell>
            <TableCell align="right">{data.bikeInfo.manufactureYear}</TableCell>
            <TableCell align="right">{data.bikeInfo.version}</TableCell>
            <TableCell align="right">{pad(data.bikeInfo.serialNumber, 6)}</TableCell>
        </TableRow>
    )
}

function ResultsTable(serialCodes) {
    const classes = useStyles();

    console.log(serialCodes)

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} aria-label="simple table">
                <TableHead>
                    <TableRow>
                        <TableCell>Serial Code</TableCell>
                        <TableCell>Model</TableCell>
                        <TableCell align="right">Model Year</TableCell>
                        <TableCell align="right">Manufacture Month</TableCell>
                        <TableCell align="right">Manufacture Year</TableCell>
                        <TableCell align="right">Version</TableCell>
                        <TableCell align="right">Serial Number</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {serialCodes.serialCodes.map((row) => (
                        <ResultRow serialCode={row} />
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}

function App() {
    const classes = useStyles();



    const [state, setState] = useState(["WBO19J101713", "SB419J100413"]);

    return (
        <div className={classes.root}>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6" className={classes.title}>
                        Serial Number Tool
                        </Typography>
                    <Button color="inherit">Login</Button>
                </Toolbar>
            </AppBar>

            <Container maxWidth="md">
                <Paper>
                    <TextField
                        id="input-serial-codes"
                        label="Serial Codes"
                        multiline
                        rows={4}
                        defaultValue="WBO19J101713, SB419J100413"
                        fullWidth
                    />
                    <Grid container alignItems="flex-start" justify="flex-end" direction="row">
                        <Button variant="contained" color="secondary" onClick={() => {
                            var items = document.getElementById("input-serial-codes").value.replace(/\n/g, ",").replace(/\s+/g, '').split(",");
                            items = items.filter(function (el) {
                                return el !== "";
                              });
                            console.log(items)
                            setState(items);
                        }}>
                            Submit
                            </Button>
                    </Grid>

                    <ResultsTable serialCodes={state} />
                </Paper>
            </Container>
        </div>
    );
}

export default App;
