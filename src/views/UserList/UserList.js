import React from 'react';
import { makeStyles } from '@material-ui/styles';
import { Grid } from '@material-ui/core';
import OnGoingTasks from 'views/Dashboard/components/OngoingTasks/onGoingTasks';
import FullFilledTasks from 'views/Dashboard/components/OngoingTasks/FulFilledTasks';
import PendingTasks from 'views/Dashboard/components/OngoingTasks/PendingTasks';

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(3)
  },
  content: {
    marginTop: theme.spacing(2)
  }
}));

const UserList = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid
        container
        spacing={4}
      >
        <Grid
          item
          lg={4}
          sm={4}
          xl={4}
          xs={12}
        >
          <FullFilledTasks />
        </Grid>
        <Grid
          item
          lg={4}
          sm={4}
          xl={4}
          xs={12}
        >
          <OnGoingTasks />
        </Grid>
        <Grid
          item
          lg={4}
          sm={4}
          xl={4}
          xs={12}
        >
          <PendingTasks />
        </Grid>
      </Grid>
    </div>
  );
};

export default UserList;
