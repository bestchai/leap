import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Button from "../Button/Button";

class QuestionTable extends React.Component {

    constructor(props) {
        super(props);
        this.state = {buttonState: ""};
        this.useStyles = {
            table: {
                minWidth: 650,
            },
        }
        this.classes = this.useStyles;
        this.rows = [
                this.createData(1,
                    'Count people with age greater than 64',
                    false,
                    this.props.queryResult),
        ];

    }

    returnDp(dp) {
        if (dp) {
            return "On"
        } else {
            return "Off"
        }
    }



    createData(id, question, dp, result) {
        return {id, question, dp, result};
    }

    render() {
        this.rows = [
            this.createData(1,
                'Count people with age greater than 64',
                false,
                this.props.queryResult),
        ];

        return (

            <TableContainer component={Paper}>
                <Table className={this.classes.table} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>DP</TableCell>
                            <TableCell>Question</TableCell>
                            <TableCell>Result</TableCell>
                            <TableCell>Get Result</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {this.rows.map(row => {

                            return (
                                <TableRow key={row.id}>
                                    <TableCell>{this.returnDp(row.dp)}</TableCell>
                                    <TableCell component="th" scope="row">{row.question}</TableCell>
                                    <TableCell>{row.result}</TableCell>
                                    <TableCell>
                                        {<Button className='ComputeButton'
                                                 onClick={this.props.buttonClick}
                                                 state={this.props.buttonState}
                                                 text={"Compute"}
                                                 ref={this.props.buttonRef}
                                        />}
                                    </TableCell>
                                </TableRow>)
                        })}
                    </TableBody>
                </Table>
            </TableContainer>
        )
    }
}

export default QuestionTable