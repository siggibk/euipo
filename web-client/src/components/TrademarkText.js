import { Typography } from "@material-ui/core"

export const TrademarkText = ({ label, text }) => {

  return (
    <div>
      <Typography variant="h6" color="textSecondary">
        {label}
      </Typography>
      <Typography color="primary">
        {text ? text : 'no data'}
      </Typography>
    </div>   
  )
}