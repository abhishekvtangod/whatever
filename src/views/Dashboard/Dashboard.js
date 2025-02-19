import React from 'react';
import { makeStyles } from '@material-ui/styles';
import { Grid } from '@material-ui/core';

import {
  Budget,
  TotalUsers,
  TasksProgress,
  TotalProfit,
  LatestSales,
  UsersByDevice
} from './components';
import OrdersFullfilled from './components/TotalProfit/OrdersFulfilled/OrdersFulfilled';
import OrdersOngoing from './components/TotalProfit/OrdersOngoing/OrdersOngoing';
import OrdersPending from './components/TotalProfit/OrdersPending/OrdersPending';

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(4)
  }
}));

const Dashboard = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid
        container
        spacing={4}
      >
        <Grid
          item
          lg={6}
          sm={6}
          xl={6}
          xs={12}
        >
          <Budget />
        </Grid>
        <Grid
          item
          lg={6}
          sm={6}
          xl={6}
          xs={12}
        >
          <TotalUsers />
        </Grid>
        <Grid
          item
          lg={6}
          sm={6}
          xl={6}
          xs={12}
        >
          <TasksProgress />
        </Grid>
        <Grid
          item
          lg={6}
          sm={6}
          xl={6}
          xs={12}
        >
          <TotalProfit />
        </Grid>
        <Grid
          item
          lg={4}
          sm={4}
          xl={4}
          xs={12}
        >
          <OrdersFullfilled />
        </Grid>
        <Grid
          item
          lg={4}
          sm={4}
          xl={4}
          xs={12}
        >
          <OrdersOngoing />
        </Grid>
        <Grid
          item
          lg={4}
          sm={4}
          xl={4}
          xs={12}
        >
          <OrdersPending />
        </Grid>
        <Grid
          item
          lg={8}
          md={12}
          xl={9}
          xs={12}
        >
          <LatestSales />
        </Grid>
        <Grid
          item
          lg={4}
          md={6}
          xl={3}
          xs={12}
        >
          <UsersByDevice />
        </Grid>
      </Grid>
    </div>
  );
};

export default Dashboard;
