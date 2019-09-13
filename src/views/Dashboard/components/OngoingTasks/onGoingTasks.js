import React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/styles';
import { Card, CardContent, Grid, Typography } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
  root: {
    height: '100%'
  },
  content: {
    alignItems: 'center',
    display: 'flex'
  },
  title: {
    fontWeight: 700
  },
  avatar: {
    backgroundColor: theme.palette.success.main,
    height: 56,
    width: 56
  },
  icon: {
    height: 32,
    width: 32
  },
  difference: {
    marginTop: theme.spacing(2),
    display: 'flex',
    alignItems: 'center'
  },
  differenceIcon: {
    color: theme.palette.success.dark
  },
  differenceValue: {
    color: theme.palette.success.dark,
    marginRight: theme.spacing(1)
  }
}));

const OnGoingTasks = props => {
  const { className, ...rest } = props;

  const classes = useStyles();

  return (
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <CardContent>
        <Grid
          container
          justify="space-between"
        >
          <Grid item>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
              variant="h1"
            >
              On Going Tasks{' '}
            </Typography>
            <Typography
              color="textSecondary"
              variant="h4"
            >
              Date of Delivery: 2_11_2018
            </Typography>
            <Typography
              color="textSecondary"
              variant="h4"
            >
              No of Fullfilled Tasks: 94{' '}
            </Typography>{' '}
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
};

OnGoingTasks.propTypes = {
  className: PropTypes.string
};

export default OnGoingTasks;
